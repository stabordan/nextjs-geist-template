## Custom screens for the chat novel interface

################################################################################
## Phone Interface Screens
################################################################################

## Phone Home Screen
screen phone_home():
    tag menu
    
    # Phone frame background
    add "#000000"
    
    frame:
        style "phone_frame"
        xalign 0.5
        yalign 0.5
        xsize 720
        ysize 1280
        
        vbox:
            # Status bar
            frame:
                style "status_bar"
                xfill True
                ysize 60
                
                hbox:
                    xfill True
                    
                    text "[phone_time]":
                        style "status_text"
                        xalign 0.0
                    
                    hbox:
                        xalign 1.0
                        spacing 10
                        
                        # Signal strength
                        for i in range(phone_signal):
                            text "●":
                                style "signal_dot"
                        
                        # Battery
                        text "[phone_battery]%":
                            style "battery_text"
            
            # App grid
            frame:
                style "app_grid_frame"
                xfill True
                yfill True
                
                vbox:
                    spacing 40
                    xalign 0.5
                    yalign 0.5
                    
                    # Messages app
                    textbutton "Messages":
                        style "app_button"
                        action Show("contacts_list")
                    
                    # Contacts app  
                    textbutton "Contacts":
                        style "app_button"
                        action Show("character_profiles")
                    
                    # Settings app
                    textbutton "Settings":
                        style "app_button"
                        action ShowMenu("preferences")
                    
                    # Gallery app
                    textbutton "Gallery":
                        style "app_button"
                        action Show("gallery_screen")

## Contacts List Screen
screen contacts_list():
    tag menu
    
    add "#000000"
    
    frame:
        style "phone_frame"
        xalign 0.5
        yalign 0.5
        xsize 720
        ysize 1280
        
        vbox:
            # Header
            frame:
                style "chat_header"
                xfill True
                ysize 80
                
                hbox:
                    xfill True
                    yalign 0.5
                    
                    textbutton "← Back":
                        style "back_button"
                        action Show("phone_home")
                    
                    text "Messages":
                        style "header_title"
                        xalign 0.5
            
            # Chat list
            viewport:
                scrollbars "vertical"
                mousewheel True
                
                vbox:
                    spacing 5
                    
                    for chat_id, chat_info in chat_rooms.items():
                        frame:
                            style "contact_button"
                            xfill True
                            ysize 80
                            
                            button:
                                style "contact_item_button"
                                xfill True
                                yfill True
                                action [
                                    SetVariable("current_chat_partner", chat_id),
                                    Show("chat_interface", partner=chat_id)
                                ]
                                
                                hbox:
                                    spacing 15
                                    yalign 0.5
                                    
                                    # Avatar placeholder
                                    frame:
                                        style "avatar_frame"
                                        xsize 50
                                        ysize 50
                                        
                                        text chat_info["name"][0]:
                                            style "avatar_text"
                                            xalign 0.5
                                            yalign 0.5
                                    
                                    vbox:
                                        spacing 5
                                        
                                        hbox:
                                            text chat_info["name"]:
                                                style "contact_name"
                                            
                                            if chat_info["online"]:
                                                text "●":
                                                    style "online_indicator"
                                        
                                        text chat_info["last_message"]:
                                            style "last_message"
                                            text_align 0.0
                                    
                                    vbox:
                                        xalign 1.0
                                        spacing 5
                                        
                                        text chat_info["last_time"]:
                                            style "message_time"
                                        
                                        if chat_info["unread"] > 0:
                                            frame:
                                                style "unread_badge"
                                                
                                                text str(chat_info["unread"]):
                                                    style "unread_text"

## Chat Interface Screen
screen chat_interface(partner):
    tag menu
    
    add "#000000"
    
    frame:
        style "phone_frame"
        xalign 0.5
        yalign 0.5
        xsize 720
        ysize 1280
        
        vbox:
            # Chat header
            frame:
                style "chat_header"
                xfill True
                ysize 80
                
                hbox:
                    xfill True
                    yalign 0.5
                    spacing 15
                    
                    textbutton "← Back":
                        style "back_button"
                        action Show("contacts_list")
                    
                    # Partner info
                    if partner in chat_rooms:
                        frame:
                            style "avatar_frame"
                            xsize 40
                            ysize 40
                            
                            text chat_rooms[partner]["name"][0]:
                                style "avatar_text_small"
                                xalign 0.5
                                yalign 0.5
                        
                        vbox:
                            spacing 2
                            
                            text chat_rooms[partner]["name"]:
                                style "chat_partner_name"
                            
                            if chat_rooms[partner]["online"]:
                                text "Online":
                                    style "online_status"
                            else:
                                text "Last seen recently":
                                    style "offline_status"
            
            # Chat messages area
            viewport:
                id "chat_viewport"
                scrollbars "vertical"
                mousewheel True
                xfill True
                yfill True
                
                vbox:
                    spacing 10
                    xfill True
                    
                    # Display chat history
                    for message in chat_history:
                        if message["type"] == MESSAGE_SENT:
                            frame:
                                style "chat_bubble_sent"
                                xalign 1.0
                                xmaximum 500
                                
                                vbox:
                                    text message["message"]:
                                        style "chat_text_sent"
                                    
                                    text message["timestamp"]:
                                        style "chat_time_sent"
                                        xalign 1.0
                        
                        elif message["type"] == MESSAGE_RECEIVED:
                            frame:
                                style "chat_bubble_received"
                                xalign 0.0
                                xmaximum 500
                                
                                vbox:
                                    text message["message"]:
                                        style "chat_text_received"
                                    
                                    text message["timestamp"]:
                                        style "chat_time_received"
                                        xalign 0.0
                        
                        elif message["type"] == MESSAGE_SYSTEM:
                            text message["message"]:
                                style "system_message"
                                xalign 0.5
                    
                    # Typing indicator
                    if someone_typing:
                        frame:
                            style "typing_bubble"
                            xalign 0.0
                            
                            text "[typing_character] is typing...":
                                style "typing_indicator"
            
            # Message input area (for visual purposes)
            frame:
                style "input_frame"
                xfill True
                ysize 60
                
                hbox:
                    xfill True
                    yalign 0.5
                    spacing 10
                    
                    text "Type a message...":
                        style "input_placeholder"
                        xfill True
                    
                    textbutton "Send":
                        style "send_button"
                        action NullAction()

## Character Profiles Screen
screen character_profiles():
    tag menu
    
    add "#000000"
    
    frame:
        style "phone_frame"
        xalign 0.5
        yalign 0.5
        xsize 720
        ysize 1280
        
        vbox:
            # Header
            frame:
                style "chat_header"
                xfill True
                ysize 80
                
                hbox:
                    xfill True
                    yalign 0.5
                    
                    textbutton "← Back":
                        style "back_button"
                        action Show("phone_home")
                    
                    text "Contacts":
                        style "header_title"
                        xalign 0.5
            
            # Character profiles
            viewport:
                scrollbars "vertical"
                mousewheel True
                
                vbox:
                    spacing 20
                    
                    for char_id, char_info in character_info.items():
                        frame:
                            style "profile_card"
                            xfill True
                            
                            vbox:
                                spacing 15
                                
                                hbox:
                                    spacing 15
                                    
                                    # Avatar
                                    frame:
                                        style "profile_avatar"
                                        xsize 80
                                        ysize 80
                                        
                                        text char_info["full_name"][0]:
                                            style "profile_avatar_text"
                                            xalign 0.5
                                            yalign 0.5
                                    
                                    vbox:
                                        spacing 5
                                        
                                        text char_info["full_name"]:
                                            style "profile_name"
                                        
                                        text char_info["occupation"]:
                                            style "profile_occupation"
                                        
                                        text "Age: [char_info[age]]":
                                            style "profile_detail"
                                        
                                        text "Relationship: [get_relationship_level(char_id)]":
                                            style "profile_relationship"
                                
                                text char_info["bio"]:
                                    style "profile_bio"
                                    text_align 0.0
                                
                                text char_info["status"]:
                                    style "profile_status"

## Gallery Screen
screen gallery_screen():
    tag menu
    
    add "#000000"
    
    frame:
        style "phone_frame"
        xalign 0.5
        yalign 0.5
        xsize 720
        ysize 1280
        
        vbox:
            # Header
            frame:
                style "chat_header"
                xfill True
                ysize 80
                
                hbox:
                    xfill True
                    yalign 0.5
                    
                    textbutton "← Back":
                        style "back_button"
                        action Show("phone_home")
                    
                    text "Gallery":
                        style "header_title"
                        xalign 0.5
            
            # Gallery content
            viewport:
                scrollbars "vertical"
                mousewheel True
                
                vbox:
                    spacing 20
                    
                    text "Memories":
                        style "gallery_section_title"
                    
                    # Achievement gallery
                    if achievements:
                        vbox:
                            spacing 10
                            
                            for achievement in achievements:
                                frame:
                                    style "achievement_frame"
                                    xfill True
                                    
                                    text "Achievement: [achievement]":
                                        style "achievement_text"
                    else:
                        text "No memories yet. Keep chatting to unlock them!":
                            style "empty_gallery_text"
                    
                    text "Story Progress":
                        style "gallery_section_title"
                    
                    frame:
                        style "progress_frame"
                        xfill True
                        
                        vbox:
                            spacing 10
                            
                            text "Day: [story_day]":
                                style "progress_text"
                            
                            text "Chapter: [story_chapter]":
                                style "progress_text"
                            
                            text "Endings Unlocked: [len(endings_unlocked)]":
                                style "progress_text"

## Notification Screen
screen notifications():
    tag menu
    
    add "#000000"
    
    frame:
        style "phone_frame"
        xalign 0.5
        yalign 0.5
        xsize 720
        ysize 1280
        
        vbox:
            # Header
            frame:
                style "chat_header"
                xfill True
                ysize 80
                
                hbox:
                    xfill True
                    yalign 0.5
                    
                    textbutton "← Back":
                        style "back_button"
                        action Show("phone_home")
                    
                    text "Notifications":
                        style "header_title"
                        xalign 0.5
                    
                    textbutton "Clear All":
                        style "clear_button"
                        action Function(clear_notifications)
            
            # Notifications list
            if notifications:
                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    
                    vbox:
                        spacing 10
                        
                        for i, notif in enumerate(notifications):
                            frame:
                                style "notification_frame"
                                xfill True
                                
                                button:
                                    style "notification_button"
                                    xfill True
                                    action Function(mark_notification_read, i)
                                    
                                    vbox:
                                        spacing 5
                                        
                                        hbox:
                                            text notif["title"]:
                                                style "notification_title"
                                            
                                            text notif["timestamp"]:
                                                style "notification_time"
                                                xalign 1.0
                                        
                                        text notif["message"]:
                                            style "notification_message"
                                        
                                        if not notif["read"]:
                                            text "●":
                                                style "unread_dot"
                                                xalign 1.0
            else:
                text "No notifications":
                    style "empty_notifications"
                    xalign 0.5
                    yalign 0.5

################################################################################
## Custom Screen Styles
################################################################################

style phone_frame:
    background "#1a1a1a"
    padding (0, 0)

style status_bar:
    background "#000000"
    padding (20, 10)

style status_text:
    color "#ffffff"
    size 16
    bold True

style signal_dot:
    color "#00ff00"
    size 12

style battery_text:
    color "#ffffff"
    size 14

style app_grid_frame:
    background "#1a1a1a"
    padding (40, 40)

style app_button:
    background "#2a2a2a"
    hover_background "#3a3a3a"
    padding (20, 15)
    margin (10, 10)
    xsize 200
    ysize 60

style app_button_text:
    color "#ffffff"
    size 18
    xalign 0.5
    yalign 0.5

style chat_header:
    background "#2a2a2a"
    padding (20, 10)

style back_button:
    background None
    hover_background "#3a3a3a"
    padding (10, 5)

style back_button_text:
    color "#0099ff"
    size 16

style header_title:
    color "#ffffff"
    size 20
    bold True

style contact_item_button:
    background None
    hover_background "#2a2a2a"
    padding (15, 10)

style avatar_frame:
    background "#0099ff"

style avatar_text:
    color "#ffffff"
    size 20
    bold True

style avatar_text_small:
    color "#ffffff"
    size 16
    bold True

style contact_name:
    color "#ffffff"
    size 18
    bold True

style online_indicator:
    color "#00ff00"
    size 12

style last_message:
    color "#888888"
    size 14
    xmaximum 300

style message_time:
    color "#666666"
    size 12

style unread_badge:
    background "#ff4444"
    padding (5, 2)
    xsize 20
    ysize 20

style unread_text:
    color "#ffffff"
    size 12
    xalign 0.5
    yalign 0.5

style chat_partner_name:
    color "#ffffff"
    size 16
    bold True

style online_status:
    color "#00ff00"
    size 12

style offline_status:
    color "#888888"
    size 12

style chat_bubble_sent:
    background "#0099ff"
    padding (15, 10)
    margin (50, 5, 10, 5)

style chat_bubble_received:
    background "#333333"
    padding (15, 10)
    margin (10, 5, 50, 5)

style chat_text_sent:
    color "#ffffff"
    size 16
    text_align 0.0

style chat_text_received:
    color "#ffffff"
    size 16
    text_align 0.0

style chat_time_sent:
    color "#cccccc"
    size 12

style chat_time_received:
    color "#cccccc"
    size 12

style system_message:
    color "#888888"
    size 14
    italic True

style typing_bubble:
    background "#333333"
    padding (15, 10)
    margin (10, 5, 50, 5)

style typing_indicator:
    color "#0099ff"
    size 14
    italic True

style input_frame:
    background "#2a2a2a"
    padding (15, 10)

style input_placeholder:
    color "#888888"
    size 16

style send_button:
    background "#0099ff"
    hover_background "#0077cc"
    padding (15, 10)

style send_button_text:
    color "#ffffff"
    size 16

style profile_card:
    background "#2a2a2a"
    padding (20, 15)
    margin (10, 5)

style profile_avatar:
    background "#0099ff"

style profile_avatar_text:
    color "#ffffff"
    size 24
    bold True

style profile_name:
    color "#ffffff"
    size 20
    bold True

style profile_occupation:
    color "#0099ff"
    size 16

style profile_detail:
    color "#cccccc"
    size 14

style profile_relationship:
    color "#00ff00"
    size 14
    bold True

style profile_bio:
    color "#cccccc"
    size 14
    xmaximum 500

style profile_status:
    color "#888888"
    size 12
    italic True

style gallery_section_title:
    color "#ffffff"
    size 18
    bold True

style achievement_frame:
    background "#2a2a2a"
    padding (15, 10)
    margin (5, 2)

style achievement_text:
    color "#00ff00"
    size 14

style empty_gallery_text:
    color "#888888"
    size 14
    italic True

style progress_frame:
    background "#2a2a2a"
    padding (15, 10)

style progress_text:
    color "#ffffff"
    size 14

style notification_frame:
    background "#2a2a2a"
    padding (15, 10)
    margin (5, 2)

style notification_button:
    background None
    hover_background "#3a3a3a"
    padding (10, 5)

style notification_title:
    color "#ffffff"
    size 16
    bold True

style notification_time:
    color "#888888"
    size 12

style notification_message:
    color "#cccccc"
    size 14

style unread_dot:
    color "#ff4444"
    size 16

style empty_notifications:
    color "#888888"
    size 16
    italic True

style clear_button:
    background "#ff4444"
    hover_background "#cc3333"
    padding (10, 5)

style clear_button_text:
    color "#ffffff"
    size 14
