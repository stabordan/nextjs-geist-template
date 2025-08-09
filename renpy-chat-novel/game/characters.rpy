## Character definitions for the chat novel

# Define character colors for chat interface
define gui.chat_color_player = "#0099ff"
define gui.chat_color_alex = "#ff6b6b"
define gui.chat_color_sam = "#4ecdc4"
define gui.chat_color_riley = "#45b7d1"
define gui.chat_color_system = "#888888"

# Character definitions
define player = Character("[player_name]", color=gui.chat_color_player)
define alex = Character("Alex", color=gui.chat_color_alex)
define sam = Character("Sam", color=gui.chat_color_sam)
define riley = Character("Riley", color=gui.chat_color_riley)
define system = Character("System", color=gui.chat_color_system)

# Default player name
default player_name = "You"

# Character relationship variables
default alex_relationship = 0
default sam_relationship = 0
default riley_relationship = 0

# Character status variables
default alex_online = True
default sam_online = True
default riley_online = False

# Chat history storage
default chat_history = []
default current_chat_partner = None

# Typing indicator variables
default someone_typing = False
default typing_character = ""

# Phone interface variables
default phone_battery = 85
default phone_signal = 4
default phone_time = "14:30"

# Story progress variables
default story_day = 1
default story_chapter = 1
default endings_unlocked = []

# Achievement system
default achievements = []

# Character information
define character_info = {
    "alex": {
        "full_name": "Alex Chen",
        "age": 22,
        "occupation": "Art Student",
        "bio": "Creative and passionate about digital art. Always up for deep conversations about life and dreams.",
        "avatar": "images/avatars/alex.png",
        "status": "Sketching new ideas ✏️"
    },
    "sam": {
        "full_name": "Sam Rodriguez",
        "age": 24,
        "occupation": "Software Developer",
        "bio": "Tech enthusiast who loves coding and gaming. Has a dry sense of humor and enjoys philosophical debates.",
        "avatar": "images/avatars/sam.png",
        "status": "Debugging life 🐛"
    },
    "riley": {
        "full_name": "Riley Park",
        "age": 21,
        "occupation": "Music Producer",
        "bio": "Aspiring musician with a love for indie rock and electronic beats. Often busy with studio sessions.",
        "avatar": "images/avatars/riley.png",
        "status": "In the studio 🎵"
    }
}

# Chat room definitions
define chat_rooms = {
    "alex": {
        "name": "Alex Chen",
        "last_message": "Hey! How was your day?",
        "last_time": "2 min ago",
        "unread": 1,
        "online": True
    },
    "sam": {
        "name": "Sam Rodriguez", 
        "last_message": "Check out this cool project I'm working on",
        "last_time": "15 min ago",
        "unread": 0,
        "online": True
    },
    "riley": {
        "name": "Riley Park",
        "last_message": "Sorry, busy with recording today",
        "last_time": "2 hours ago", 
        "unread": 0,
        "online": False
    },
    "group": {
        "name": "Study Group",
        "last_message": "Sam: Anyone free for coffee tomorrow?",
        "last_time": "1 hour ago",
        "unread": 3,
        "online": True
    }
}

# Message types for different chat styles
define MESSAGE_SENT = "sent"
define MESSAGE_RECEIVED = "received"
define MESSAGE_SYSTEM = "system"
define MESSAGE_TYPING = "typing"

# Initialize character sprites (placeholder paths)
image alex neutral = "images/characters/alex_neutral.png"
image alex happy = "images/characters/alex_happy.png"
image alex sad = "images/characters/alex_sad.png"
image alex surprised = "images/characters/alex_surprised.png"

image sam neutral = "images/characters/sam_neutral.png"
image sam happy = "images/characters/sam_happy.png"
image sam thinking = "images/characters/sam_thinking.png"
image sam excited = "images/characters/sam_excited.png"

image riley neutral = "images/characters/riley_neutral.png"
image riley happy = "images/characters/riley_happy.png"
image riley tired = "images/characters/riley_tired.png"
image riley focused = "images/characters/riley_focused.png"

# Background images
image bg phone_home = "images/backgrounds/phone_home.png"
image bg chat_background = "images/backgrounds/chat_bg.png"
image bg contacts_list = "images/backgrounds/contacts_bg.png"

# UI elements
image ui phone_frame = "images/ui/phone_frame.png"
image ui status_bar = "images/ui/status_bar.png"
image ui chat_bubble_sent = "images/ui/bubble_sent.png"
image ui chat_bubble_received = "images/ui/bubble_received.png"

# Sound effects
define audio.message_send = "audio/sfx/message_send.ogg"
define audio.message_receive = "audio/sfx/message_receive.ogg"
define audio.typing_sound = "audio/sfx/typing.ogg"
define audio.notification = "audio/sfx/notification.ogg"

# Background music
define audio.main_theme = "audio/music/main_theme.ogg"
define audio.chat_ambient = "audio/music/chat_ambient.ogg"
define audio.emotional_theme = "audio/music/emotional.ogg"

# Functions for character interactions
init python:
    def add_relationship_points(character, points):
        """Add relationship points to a character"""
        if character == "alex":
            store.alex_relationship += points
        elif character == "sam":
            store.sam_relationship += points
        elif character == "riley":
            store.riley_relationship += points
    
    def get_relationship_level(character):
        """Get the relationship level with a character"""
        if character == "alex":
            points = store.alex_relationship
        elif character == "sam":
            points = store.sam_relationship
        elif character == "riley":
            points = store.riley_relationship
        else:
            return "Unknown"
        
        if points >= 50:
            return "Best Friend"
        elif points >= 30:
            return "Close Friend"
        elif points >= 15:
            return "Good Friend"
        elif points >= 5:
            return "Friend"
        elif points >= 0:
            return "Acquaintance"
        else:
            return "Distant"
    
    def add_chat_message(sender, message, message_type="received"):
        """Add a message to chat history"""
        import datetime
        timestamp = datetime.datetime.now().strftime("%H:%M")
        
        chat_entry = {
            "sender": sender,
            "message": message,
            "type": message_type,
            "timestamp": timestamp
        }
        
        store.chat_history.append(chat_entry)
    
    def unlock_achievement(achievement_id, achievement_name):
        """Unlock an achievement"""
        if achievement_id not in store.achievements:
            store.achievements.append(achievement_id)
            renpy.notify("Achievement Unlocked: " + achievement_name)
    
    def set_character_online(character, online_status):
        """Set a character's online status"""
        if character == "alex":
            store.alex_online = online_status
        elif character == "sam":
            store.sam_online = online_status
        elif character == "riley":
            store.riley_online = online_status
        
        # Update chat rooms status
        if character in store.chat_rooms:
            store.chat_rooms[character]["online"] = online_status
    
    def start_typing_indicator(character):
        """Show typing indicator for a character"""
        store.someone_typing = True
        store.typing_character = character
    
    def stop_typing_indicator():
        """Hide typing indicator"""
        store.someone_typing = False
        store.typing_character = ""
    
    def get_character_avatar(character):
        """Get character avatar path"""
        if character in character_info:
            return character_info[character]["avatar"]
        return "images/avatars/default.png"
    
    def get_character_status(character):
        """Get character status message"""
        if character in character_info:
            return character_info[character]["status"]
        return "Available"
    
    def update_chat_room_info(character, last_message, unread_count=0):
        """Update chat room information"""
        import datetime
        current_time = datetime.datetime.now().strftime("%H:%M")
        
        if character in store.chat_rooms:
            store.chat_rooms[character]["last_message"] = last_message
            store.chat_rooms[character]["last_time"] = current_time
            store.chat_rooms[character]["unread"] = unread_count

# Character mood system
default character_moods = {
    "alex": "neutral",
    "sam": "neutral", 
    "riley": "neutral"
}

init python:
    def set_character_mood(character, mood):
        """Set character mood for sprite display"""
        store.character_moods[character] = mood
    
    def get_character_sprite(character):
        """Get current character sprite based on mood"""
        mood = store.character_moods.get(character, "neutral")
        return f"{character} {mood}"

# Notification system
default notifications = []

init python:
    def add_notification(title, message, character=None):
        """Add a notification to the notification list"""
        import datetime
        timestamp = datetime.datetime.now().strftime("%H:%M")
        
        notification = {
            "title": title,
            "message": message,
            "character": character,
            "timestamp": timestamp,
            "read": False
        }
        
        store.notifications.append(notification)
        
        # Play notification sound
        renpy.music.play(audio.notification, channel="sound")
    
    def mark_notification_read(index):
        """Mark a notification as read"""
        if 0 <= index < len(store.notifications):
            store.notifications[index]["read"] = True
    
    def clear_notifications():
        """Clear all notifications"""
        store.notifications = []

# Story branching system
default story_flags = {
    "met_alex": False,
    "met_sam": False,
    "met_riley": False,
    "first_group_chat": False,
    "alex_confession": False,
    "sam_project_help": False,
    "riley_concert_invite": False,
    "love_triangle_started": False,
    "ending_chosen": None
}

init python:
    def set_story_flag(flag_name, value=True):
        """Set a story flag"""
        store.story_flags[flag_name] = value
    
    def get_story_flag(flag_name):
        """Get a story flag value"""
        return store.story_flags.get(flag_name, False)
    
    def check_ending_requirements():
        """Check which endings are available based on story flags and relationships"""
        available_endings = []
        
        # Alex ending
        if store.alex_relationship >= 40 and get_story_flag("alex_confession"):
            available_endings.append("alex_ending")
        
        # Sam ending  
        if store.sam_relationship >= 40 and get_story_flag("sam_project_help"):
            available_endings.append("sam_ending")
        
        # Riley ending
        if store.riley_relationship >= 35 and get_story_flag("riley_concert_invite"):
            available_endings.append("riley_ending")
        
        # Friendship ending
        if (store.alex_relationship >= 20 and 
            store.sam_relationship >= 20 and 
            store.riley_relationship >= 20):
            available_endings.append("friendship_ending")
        
        # Alone ending (always available)
        available_endings.append("alone_ending")
        
        return available_endings
