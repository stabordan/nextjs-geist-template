## The main script file for the Chat Novel

# Game starts here
label start:
    
    # Initialize the game
    $ quick_menu = False
    
    # Set up initial game state
    $ player_name = renpy.input("What's your name?", length=20)
    $ player_name = player_name.strip()
    
    if player_name == "":
        $ player_name = "You"
    
    # Play background music
    play music audio.main_theme fadein 2.0
    
    # Show phone interface
    scene bg phone_home
    show screen phone_home
    
    # Initial setup
    $ set_story_flag("game_started", True)
    $ story_day = 1
    $ story_chapter = 1
    
    # Add initial notification
    $ add_notification("Welcome!", "Welcome to your new phone, [player_name]!")
    
    # Tutorial message
    "Welcome to Chat Novel!"
    "You've just got a new phone and some interesting people want to chat with you."
    "Navigate through your messages to start conversations and build relationships."
    "Your choices will determine how the story unfolds."
    
    # First day introduction
    $ add_chat_message("system", "Welcome to your messaging app!", MESSAGE_SYSTEM)
    
    # Set initial character states
    $ set_character_online("alex", True)
    $ set_character_online("sam", True) 
    $ set_character_online("riley", False)
    
    # Update chat rooms with initial messages
    $ update_chat_room_info("alex", "Hey! I saw you got a new number 😊", 1)
    $ update_chat_room_info("sam", "Welcome to the group! I'm Sam", 1)
    $ update_chat_room_info("riley", "Sorry, busy with recording today", 0)
    
    # Show the phone interface and wait for player interaction
    call screen phone_home
    
    return

# Alex's chat storyline
label alex_chat:
    
    # Clear previous chat history for this conversation
    $ chat_history = []
    $ current_chat_partner = "alex"
    
    # Set Alex's mood
    $ set_character_mood("alex", "happy")
    
    # Add initial messages to chat
    $ add_chat_message("alex", "Hey! I saw you got a new number 😊", MESSAGE_RECEIVED)
    $ add_chat_message("alex", "I'm Alex, by the way. We're in the same art class!", MESSAGE_RECEIVED)
    
    # Show chat interface
    call screen chat_interface("alex")
    
    # Player's response options
    menu:
        "Hi Alex! Nice to meet you properly!":
            $ add_chat_message(player_name, "Hi Alex! Nice to meet you properly!", MESSAGE_SENT)
            $ add_relationship_points("alex", 3)
            $ add_chat_message("alex", "Aww, you're so sweet! I've been wanting to talk to you for a while 💕", MESSAGE_RECEIVED)
            
        "Oh hey, you're the one who sits in the back row?":
            $ add_chat_message(player_name, "Oh hey, you're the one who sits in the back row?", MESSAGE_SENT)
            $ add_relationship_points("alex", 1)
            $ add_chat_message("alex", "Haha yeah, that's me! I like to observe everyone's art styles from there", MESSAGE_RECEIVED)
            
        "How did you get my number?":
            $ add_chat_message(player_name, "How did you get my number?", MESSAGE_SENT)
            $ add_relationship_points("alex", -1)
            $ set_character_mood("alex", "surprised")
            $ add_chat_message("alex", "Oh! Sam gave it to me, hope that's okay? 😅", MESSAGE_RECEIVED)
    
    # Continue conversation
    $ start_typing_indicator("alex")
    pause 2.0
    $ stop_typing_indicator()
    
    $ add_chat_message("alex", "So... what kind of art do you like to create?", MESSAGE_RECEIVED)
    
    menu:
        "I love digital art and character design":
            $ add_chat_message(player_name, "I love digital art and character design", MESSAGE_SENT)
            $ add_relationship_points("alex", 4)
            $ set_character_mood("alex", "excited")
            $ add_chat_message("alex", "OMG YES! That's exactly what I do! We should collaborate sometime! ✨", MESSAGE_RECEIVED)
            $ set_story_flag("alex_art_interest", True)
            
        "I'm more into traditional painting":
            $ add_chat_message(player_name, "I'm more into traditional painting", MESSAGE_SENT)
            $ add_relationship_points("alex", 2)
            $ add_chat_message("alex", "That's so cool! I admire people who can work with traditional media", MESSAGE_RECEIVED)
            
        "I'm not really artistic":
            $ add_chat_message(player_name, "I'm not really artistic", MESSAGE_SENT)
            $ add_relationship_points("alex", 1)
            $ add_chat_message("alex", "Don't say that! Everyone has creativity in them, you just need to find your medium 😊", MESSAGE_RECEIVED)
    
    # Alex shares something personal
    $ add_chat_message("alex", "Can I tell you something?", MESSAGE_RECEIVED)
    $ add_chat_message("alex", "I've been working on this really personal art project...", MESSAGE_RECEIVED)
    $ add_chat_message("alex", "It's about finding connection in a digital world", MESSAGE_RECEIVED)
    
    menu:
        "That sounds really meaningful":
            $ add_chat_message(player_name, "That sounds really meaningful", MESSAGE_SENT)
            $ add_relationship_points("alex", 3)
            $ add_chat_message("alex", "Thank you for understanding! Most people think it's too abstract", MESSAGE_RECEIVED)
            
        "I'd love to see it sometime":
            $ add_chat_message(player_name, "I'd love to see it sometime", MESSAGE_SENT)
            $ add_relationship_points("alex", 5)
            $ set_character_mood("alex", "happy")
            $ add_chat_message("alex", "Really?! You'd be the first person I show it to 💕", MESSAGE_RECEIVED)
            $ set_story_flag("alex_art_sharing", True)
            
        "Sounds interesting":
            $ add_chat_message(player_name, "Sounds interesting", MESSAGE_SENT)
            $ add_relationship_points("alex", 1)
            $ add_chat_message("alex", "Yeah, it's been consuming my thoughts lately", MESSAGE_RECEIVED)
    
    # End of first conversation
    $ add_chat_message("alex", "I should let you explore your new phone more!", MESSAGE_RECEIVED)
    $ add_chat_message("alex", "But let's chat again soon, okay? 😊", MESSAGE_RECEIVED)
    
    # Update chat room info
    $ update_chat_room_info("alex", "But let's chat again soon, okay? 😊", 0)
    
    # Achievement check
    if alex_relationship >= 10:
        $ unlock_achievement("alex_friend", "Made friends with Alex")
    
    # Return to contacts list
    call screen contacts_list
    
    return

# Sam's chat storyline  
label sam_chat:
    
    # Clear previous chat history for this conversation
    $ chat_history = []
    $ current_chat_partner = "sam"
    
    # Set Sam's mood
    $ set_character_mood("sam", "neutral")
    
    # Add initial messages to chat
    $ add_chat_message("sam", "Welcome to the group! I'm Sam", MESSAGE_RECEIVED)
    $ add_chat_message("sam", "I handle most of the tech stuff around here", MESSAGE_RECEIVED)
    $ add_chat_message("sam", "Nice phone setup btw, good choice on the messaging app", MESSAGE_RECEIVED)
    
    # Show chat interface
    call screen chat_interface("sam")
    
    # Player's response options
    menu:
        "Thanks! Are you into programming?":
            $ add_chat_message(player_name, "Thanks! Are you into programming?", MESSAGE_SENT)
            $ add_relationship_points("sam", 3)
            $ set_character_mood("sam", "excited")
            $ add_chat_message("sam", "Absolutely! I'm working on some really cool projects right now", MESSAGE_RECEIVED)
            
        "What kind of tech stuff?":
            $ add_chat_message(player_name, "What kind of tech stuff?", MESSAGE_SENT)
            $ add_relationship_points("sam", 2)
            $ add_chat_message("sam", "Web development, mobile apps, some AI experimentation", MESSAGE_RECEIVED)
            
        "How do you know Alex?":
            $ add_chat_message(player_name, "How do you know Alex?", MESSAGE_SENT)
            $ add_relationship_points("sam", 1)
            $ add_chat_message("sam", "We met in a digital media class. Alex does the art, I do the code", MESSAGE_RECEIVED)
    
    # Sam shares their current project
    $ start_typing_indicator("sam")
    pause 2.0
    $ stop_typing_indicator()
    
    $ add_chat_message("sam", "Actually, I'm working on something that might interest you", MESSAGE_RECEIVED)
    $ add_chat_message("sam", "It's an app that helps people connect through shared interests", MESSAGE_RECEIVED)
    $ add_chat_message("sam", "Kind of like what we're doing right now, but more sophisticated", MESSAGE_RECEIVED)
    
    menu:
        "That sounds amazing! Tell me more":
            $ add_chat_message(player_name, "That sounds amazing! Tell me more", MESSAGE_SENT)
            $ add_relationship_points("sam", 4)
            $ set_character_mood("sam", "happy")
            $ add_chat_message("sam", "Really? Most people's eyes glaze over when I talk tech 😅", MESSAGE_RECEIVED)
            $ set_story_flag("sam_project_interest", True)
            
        "How does it work?":
            $ add_chat_message(player_name, "How does it work?", MESSAGE_SENT)
            $ add_relationship_points("sam", 3)
            $ add_chat_message("sam", "It uses machine learning to analyze conversation patterns and suggest compatible people", MESSAGE_RECEIVED)
            
        "Sounds complicated":
            $ add_chat_message(player_name, "Sounds complicated", MESSAGE_SENT)
            $ add_relationship_points("sam", 0)
            $ set_character_mood("sam", "thinking")
            $ add_chat_message("sam", "Yeah, it is pretty complex. But that's what makes it interesting!", MESSAGE_RECEIVED)
    
    # Sam opens up about their motivation
    $ add_chat_message("sam", "Want to know why I'm building it?", MESSAGE_RECEIVED)
    
    menu:
        "Sure, I'm curious":
            $ add_chat_message(player_name, "Sure, I'm curious", MESSAGE_SENT)
            $ add_relationship_points("sam", 2)
            $ add_chat_message("sam", "I think technology should bring people together, not isolate them", MESSAGE_RECEIVED)
            $ add_chat_message("sam", "Too many apps are designed to be addictive rather than meaningful", MESSAGE_RECEIVED)
            
        "Is it for a class project?":
            $ add_chat_message(player_name, "Is it for a class project?", MESSAGE_SENT)
            $ add_relationship_points("sam", 1)
            $ add_chat_message("sam", "Started as one, but now it's become something I really believe in", MESSAGE_RECEIVED)
    
    # Sam makes an offer
    $ add_chat_message("sam", "Hey, would you be interested in beta testing it?", MESSAGE_RECEIVED)
    $ add_chat_message("sam", "I could use feedback from someone with fresh perspective", MESSAGE_RECEIVED)
    
    menu:
        "I'd love to help!":
            $ add_chat_message(player_name, "I'd love to help!", MESSAGE_SENT)
            $ add_relationship_points("sam", 5)
            $ set_character_mood("sam", "excited")
            $ add_chat_message("sam", "Awesome! I'll send you the beta link when it's ready", MESSAGE_RECEIVED)
            $ set_story_flag("sam_beta_tester", True)
            
        "What would I need to do?":
            $ add_chat_message(player_name, "What would I need to do?", MESSAGE_SENT)
            $ add_relationship_points("sam", 2)
            $ add_chat_message("sam", "Just use it naturally and let me know what feels right or wrong", MESSAGE_RECEIVED)
            
        "I'm not really a tech person":
            $ add_chat_message(player_name, "I'm not really a tech person", MESSAGE_SENT)
            $ add_relationship_points("sam", 1)
            $ add_chat_message("sam", "That's exactly why your feedback would be valuable!", MESSAGE_RECEIVED)
    
    # End of conversation
    $ add_chat_message("sam", "Thanks for listening to me ramble about code 😅", MESSAGE_RECEIVED)
    $ add_chat_message("sam", "It's nice to have someone who actually seems interested", MESSAGE_RECEIVED)
    
    # Update chat room info
    $ update_chat_room_info("sam", "It's nice to have someone who actually seems interested", 0)
    
    # Achievement check
    if sam_relationship >= 10:
        $ unlock_achievement("sam_friend", "Connected with Sam")
    
    # Return to contacts list
    call screen contacts_list
    
    return

# Riley's chat storyline
label riley_chat:
    
    # Check if Riley is online
    if not riley_online:
        "Riley is currently offline. Try again later."
        call screen contacts_list
        return
    
    # Clear previous chat history for this conversation
    $ chat_history = []
    $ current_chat_partner = "riley"
    
    # Set Riley's mood
    $ set_character_mood("riley", "tired")
    
    # Add initial messages to chat
    $ add_chat_message("riley", "Oh hey, you're the new person everyone's talking about", MESSAGE_RECEIVED)
    $ add_chat_message("riley", "Sorry I've been MIA, been living in the studio lately", MESSAGE_RECEIVED)
    
    # Show chat interface
    call screen chat_interface("riley")
    
    # Player's response options
    menu:
        "No worries! What kind of music do you make?":
            $ add_chat_message(player_name, "No worries! What kind of music do you make?", MESSAGE_SENT)
            $ add_relationship_points("riley", 3)
            $ set_character_mood("riley", "neutral")
            $ add_chat_message("riley", "Mostly indie electronic with some rock elements", MESSAGE_RECEIVED)
            
        "Studio life sounds intense":
            $ add_chat_message(player_name, "Studio life sounds intense", MESSAGE_SENT)
            $ add_relationship_points("riley", 2)
            $ add_chat_message("riley", "It is, but it's where I feel most alive", MESSAGE_RECEIVED)
            
        "Everyone's talking about me?":
            $ add_chat_message(player_name, "Everyone's talking about me?", MESSAGE_SENT)
            $ add_relationship_points("riley", 1)
            $ add_chat_message("riley", "Haha, just Alex and Sam. They seem to like you", MESSAGE_RECEIVED)
    
    # Riley shares their current project
    $ start_typing_indicator("riley")
    pause 2.0
    $ stop_typing_indicator()
    
    $ add_chat_message("riley", "I'm working on this track that's been haunting me for weeks", MESSAGE_RECEIVED)
    $ add_chat_message("riley", "It's about digital connections and whether they're real or just illusions", MESSAGE_RECEIVED)
    
    menu:
        "That's a fascinating concept":
            $ add_chat_message(player_name, "That's a fascinating concept", MESSAGE_SENT)
            $ add_relationship_points("riley", 4)
            $ set_character_mood("riley", "happy")
            $ add_chat_message("riley", "Right? Like, are we really connecting or just exchanging data?", MESSAGE_RECEIVED)
            $ set_story_flag("riley_philosophy_interest", True)
            
        "Sounds deep":
            $ add_chat_message(player_name, "Sounds deep", MESSAGE_SENT)
            $ add_relationship_points("riley", 2)
            $ add_chat_message("riley", "Maybe too deep. Sometimes I overthink things", MESSAGE_RECEIVED)
            
        "Can I hear it sometime?":
            $ add_chat_message(player_name, "Can I hear it sometime?", MESSAGE_SENT)
            $ add_relationship_points("riley", 3)
            $ add_chat_message("riley", "When it's done, maybe. I'm pretty protective of unfinished work", MESSAGE_RECEIVED)
    
    # Riley opens up about their struggles
    $ add_chat_message("riley", "Can I be honest with you?", MESSAGE_RECEIVED)
    $ add_chat_message("riley", "Sometimes I wonder if I'm just hiding behind my music", MESSAGE_RECEIVED)
    $ add_chat_message("riley", "Like, it's easier to express feelings in songs than in real conversations", MESSAGE_RECEIVED)
    
    menu:
        "Music is just another form of communication":
            $ add_chat_message(player_name, "Music is just another form of communication", MESSAGE_SENT)
            $ add_relationship_points("riley", 4)
            $ set_character_mood("riley", "surprised")
            $ add_chat_message("riley", "I... never thought of it that way. That's actually really insightful", MESSAGE_RECEIVED)
            
        "Maybe that's okay though":
            $ add_chat_message(player_name, "Maybe that's okay though", MESSAGE_SENT)
            $ add_relationship_points("riley", 3)
            $ add_chat_message("riley", "You think so? Sometimes I feel like I should be more... direct", MESSAGE_RECEIVED)
            
        "Why do you think that is?":
            $ add_chat_message(player_name, "Why do you think that is?", MESSAGE_SENT)
            $ add_relationship_points("riley", 2)
            $ add_chat_message("riley", "I guess... words feel so permanent. Music can be interpreted differently", MESSAGE_RECEIVED)
    
    # Riley makes a surprising offer
    $ add_chat_message("riley", "You know what?", MESSAGE_RECEIVED)
    $ add_chat_message("riley", "I'm playing a small gig next week. Just a coffee shop thing", MESSAGE_RECEIVED)
    $ add_chat_message("riley", "Want to come? I could use a friendly face in the crowd", MESSAGE_RECEIVED)
    
    menu:
        "I'd love to come!":
            $ add_chat_message(player_name, "I'd love to come!", MESSAGE_SENT)
            $ add_relationship_points("riley", 5)
            $ set_character_mood("riley", "happy")
            $ add_chat_message("riley", "Really? That... that means a lot to me", MESSAGE_RECEIVED)
            $ set_story_flag("riley_concert_invite", True)
            
        "What kind of music will you play?":
            $ add_chat_message(player_name, "What kind of music will you play?", MESSAGE_SENT)
            $ add_relationship_points("riley", 2)
            $ add_chat_message("riley", "Probably some of my more accessible stuff. Save the experimental tracks for later", MESSAGE_RECEIVED)
            
        "I'm not sure if I can make it":
            $ add_chat_message(player_name, "I'm not sure if I can make it", MESSAGE_SENT)
            $ add_relationship_points("riley", 0)
            $ set_character_mood("riley", "sad")
            $ add_chat_message("riley", "Oh, okay. No pressure. Just thought I'd ask", MESSAGE_RECEIVED)
    
    # End of conversation
    $ add_chat_message("riley", "I should get back to the studio", MESSAGE_RECEIVED)
    $ add_chat_message("riley", "Thanks for the chat. It's nice to talk to someone new", MESSAGE_RECEIVED)
    
    # Update chat room info
    $ update_chat_room_info("riley", "Thanks for the chat. It's nice to talk to someone new", 0)
    
    # Achievement check
    if riley_relationship >= 10:
        $ unlock_achievement("riley_friend", "Harmonized with Riley")
    
    # Set Riley back to offline after conversation
    $ set_character_online("riley", False)
    
    # Return to contacts list
    call screen contacts_list
    
    return

# Group chat storyline
label group_chat:
    
    # Clear previous chat history for this conversation
    $ chat_history = []
    $ current_chat_partner = "group"
    
    # Add group chat messages
    $ add_chat_message("sam", "Hey everyone! Our new friend is here", MESSAGE_RECEIVED)
    $ add_chat_message("alex", "Yay! Welcome to our little group 🎉", MESSAGE_RECEIVED)
    
    if riley_online:
        $ add_chat_message("riley", "Hey there. Sam's told us good things", MESSAGE_RECEIVED)
    
    # Show chat interface
    call screen chat_interface("group")
    
    # Player's response options
    menu:
        "Thanks for welcoming me!":
            $ add_chat_message(player_name, "Thanks for welcoming me!", MESSAGE_SENT)
            $ add_relationship_points("alex", 2)
            $ add_relationship_points("sam", 2)
            $ add_relationship_points("riley", 1)
            $ add_chat_message("alex", "Aww, you're so sweet! 💕", MESSAGE_RECEIVED)
            
        "What do you all usually talk about?":
            $ add_chat_message(player_name, "What do you all usually talk about?", MESSAGE_SENT)
            $ add_relationship_points("sam", 2)
            $ add_chat_message("sam", "Everything! Art, tech, music, life philosophy...", MESSAGE_RECEIVED)
            $ add_chat_message("alex", "And lots of random memes 😂", MESSAGE_RECEIVED)
            
        "This is nice, having a group to chat with":
            $ add_chat_message(player_name, "This is nice, having a group to chat with", MESSAGE_SENT)
            $ add_relationship_points("alex", 1)
            $ add_relationship_points("sam", 1)
            $ add_relationship_points("riley", 2)
            $ add_chat_message("riley", "Yeah, it's good to have people who get it", MESSAGE_RECEIVED)
    
    # Group discussion about weekend plans
    $ add_chat_message("alex", "So what's everyone doing this weekend?", MESSAGE_RECEIVED)
    $ add_chat_message("sam", "Working on my app, as usual 🤓", MESSAGE_RECEIVED)
    
    if riley_online:
        $ add_chat_message("riley", "Studio time for me. Got that gig coming up", MESSAGE_RECEIVED)
    
    $ add_chat_message("alex", "I was thinking we could all hang out sometime?", MESSAGE_RECEIVED)
    $ add_chat_message("alex", "Like, actually meet in person? 😊", MESSAGE_RECEIVED)
    
    menu:
        "That sounds great!":
            $ add_chat_message(player_name, "That sounds great!", MESSAGE_SENT)
            $ add_relationship_points("alex", 3)
            $ add_relationship_points("sam", 2)
            $ add_relationship_points("riley", 2)
            $ add_chat_message("alex", "Yay! I know the perfect coffee shop", MESSAGE_RECEIVED)
            $ set_story_flag("group_meetup_planned", True)
            
        "I'm a bit nervous about meeting in person":
            $ add_chat_message(player_name, "I'm a bit nervous about meeting in person", MESSAGE_SENT)
            $ add_relationship_points("alex", 1)
            $ add_relationship_points("riley", 3)
            $ add_chat_message("riley", "I get that. Online feels safer sometimes", MESSAGE_RECEIVED)
            $ add_chat_message("alex", "No pressure! We can keep chatting here as long as you want", MESSAGE_RECEIVED)
            
        "Maybe sometime soon":
            $ add_chat_message(player_name, "Maybe sometime soon", MESSAGE_SENT)
            $ add_relationship_points("sam", 1)
            $ add_chat_message("sam", "No rush. We're not going anywhere", MESSAGE_RECEIVED)
    
    # Set flag for first group chat
    $ set_story_flag("first_group_chat", True)
    
    # End group chat
    $ add_chat_message("alex", "I should go work on my art project", MESSAGE_RECEIVED)
    $ add_chat_message("sam", "And I have code to debug", MESSAGE_RECEIVED)
    
    if riley_online:
        $ add_chat_message("riley", "Studio calls. Talk later everyone", MESSAGE_RECEIVED)
    
    # Update chat room info
    $ update_chat_room_info("group", "Studio calls. Talk later everyone", 0)
    
    # Achievement for first group chat
    $ unlock_achievement("group_chat", "Joined the group conversation")
    
    # Return to contacts list
    call screen contacts_list
    
    return

# Story progression and ending paths
label story_progression:
    
    # Check story progress and unlock new content
    if story_day == 1 and alex_relationship >= 5 and sam_relationship >= 5:
        $ story_day = 2
        $ add_notification("Story Progress", "New conversations unlocked!")
        
        # Riley comes online
        $ set_character_online("riley", True)
        $ update_chat_room_info("riley", "Hey, heard you've been chatting with Alex and Sam", 1)
    
    if story_day == 2 and riley_relationship >= 5:
        $ story_day = 3
        $ story_chapter = 2
        $ add_notification("Chapter 2", "Relationships are deepening...")
    
    # Check for ending conditions
    $ available_endings = check_ending_requirements()
    
    if len(available_endings) > 0 and story_day >= 3:
        jump ending_selection
    
    return

# Ending selection
label ending_selection:
    
    "As the days pass, you realize your relationships with Alex, Sam, and Riley have grown in different ways."
    "It's time to decide what matters most to you..."
    
    $ available_endings = check_ending_requirements()
    
    menu:
        "Focus on your connection with Alex" if "alex_ending" in available_endings:
            jump alex_ending
            
        "Pursue your partnership with Sam" if "sam_ending" in available_endings:
            jump sam_ending
            
        "Follow your heart with Riley" if "riley_ending" in available_endings:
            jump riley_ending
            
        "Maintain friendships with everyone" if "friendship_ending" in available_endings:
            jump friendship_ending
            
        "Focus on yourself for now":
            jump alone_ending

# Alex Ending
label alex_ending:
    
    scene bg chat_background
    
    "You decide to pursue a deeper relationship with Alex."
    "Your shared love of art and creativity has brought you closer together."
    
    # Final conversation with Alex
    $ chat_history = []
    $ add_chat_message("alex", "I have something important to tell you...", MESSAGE_RECEIVED)
    $ add_chat_message("alex", "These past few weeks chatting with you have been amazing", MESSAGE_RECEIVED)
    $ add_chat_message("alex", "I think I'm falling for you 💕", MESSAGE_RECEIVED)
    
    call screen chat_interface("alex")
    
    menu:
        "I feel the same way":
            $ add_chat_message(player_name, "I feel the same way", MESSAGE_SENT)
            $ add_chat_message("alex", "Really?! This is like a dream come true! ✨", MESSAGE_RECEIVED)
            $ add_chat_message("alex", "Want to meet up and make this official? 😊", MESSAGE_RECEIVED)
            
            "You and Alex begin a beautiful relationship, built on shared creativity and deep understanding."
            "Your love story started with a simple text message, but grew into something real and lasting."
            
        "I care about you, but as a friend":
            $ add_chat_message(player_name, "I care about you, but as a friend", MESSAGE_SENT)
            $ add_chat_message("alex", "I understand... I'm glad we can still be close friends", MESSAGE_RECEIVED)
            
            "You maintain a strong friendship with Alex, supporting each other's artistic endeavors."
            "Sometimes the best relationships are built on mutual respect and understanding."
    
    $ endings_unlocked.append("alex_ending")
    $ unlock_achievement("alex_route", "Completed Alex's storyline")
    
    jump ending_credits

# Sam Ending
label sam_ending:
    
    scene bg chat_background
    
    "You decide to partner with Sam on their ambitious project."
    "Your collaboration has grown into something deeper than just friendship."
    
    # Final conversation with Sam
    $ chat_history = []
    $ add_chat_message("sam", "The beta test results are in...", MESSAGE_RECEIVED)
    $ add_chat_message("sam", "Your feedback was incredible. You really understand what I'm trying to build", MESSAGE_RECEIVED)
    $ add_chat_message("sam", "I was wondering... would you like to be my co-founder?", MESSAGE_RECEIVED)
    
    call screen chat_interface("sam")
    
    menu:
        "I'd love to build this with you":
            $ add_chat_message(player_name, "I'd love to build this with you", MESSAGE_SENT)
            $ add_chat_message("sam", "This is going to be amazing! We make a great team 🚀", MESSAGE_RECEIVED)
            
            "You and Sam launch your app together, creating meaningful connections for people around the world."
            "Your partnership, which started online, becomes the foundation for both business and romance."
            
        "I'm honored, but I have other plans":
            $ add_chat_message(player_name, "I'm honored, but I have other plans", MESSAGE_SENT)
            $ add_chat_message("sam", "I understand. Thanks for all your help getting this far", MESSAGE_RECEIVED)
            
            "You remain close friends with Sam, watching proudly as their app becomes a success."
            "Sometimes supporting someone's dreams is the greatest gift you can give."
    
    $ endings_unlocked.append("sam_ending")
    $ unlock_achievement("sam_route", "Completed Sam's storyline")
    
    jump ending_credits

# Riley Ending
label riley_ending:
    
    scene bg chat_background
    
    "You decide to follow your heart and pursue Riley."
    "Your connection through music and deep conversations has created something special."
    
    # Final conversation with Riley
    $ chat_history = []
    $ add_chat_message("riley", "The gig went amazing, thanks to you being there", MESSAGE_RECEIVED)
    $ add_chat_message("riley", "I finished that song I was working on...", MESSAGE_RECEIVED)
    $ add_chat_message("riley", "It's about finding someone who understands your frequency 🎵", MESSAGE_RECEIVED)
    $ add_chat_message("riley", "I think that someone might be you", MESSAGE_RECEIVED)
    
    call screen chat_interface("riley")
    
    menu:
        "You're my favorite song too":
            $ add_chat_message(player_name, "You're my favorite song too", MESSAGE_SENT)
            $ add_chat_message("riley", "That's the most beautiful thing anyone's ever said to me 💕", MESSAGE_RECEIVED)
            
            "You and Riley create beautiful music together, both literally and figuratively."
            "Your love story has its own unique rhythm, perfect in its imperfection."
            
        "I'm glad I could inspire your music":
            $ add_chat_message(player_name, "I'm glad I could inspire your music", MESSAGE_SENT)
            $ add_chat_message("riley", "You've inspired more than just music... you've inspired me to be more open", MESSAGE_RECEIVED)
            
            "You and Riley maintain a deep connection, supporting each other's creative endeavors."
            "Your friendship becomes the foundation for Riley's most heartfelt compositions."
    
    $ endings_unlocked.append("riley_ending")
    $ unlock_achievement("riley_route", "Completed Riley's storyline")
    
    jump ending_credits

# Friendship Ending
label friendship_ending:
    
    scene bg chat_background
    
    "You decide that the friendships you've built are too precious to risk changing."
    "Sometimes the best relationships are the ones that don't need labels."
    
    # Group conversation
    $ chat_history = []
    $ add_chat_message("alex", "I'm so glad we all became friends", MESSAGE_RECEIVED)
    $ add_chat_message("sam", "Yeah, this group chat has become my favorite notification", MESSAGE_RECEIVED)
    $ add_chat_message("riley", "It's nice to have people who get it, you know?", MESSAGE_RECEIVED)
    $ add_chat_message("alex", "We should definitely meet up in person soon!", MESSAGE_RECEIVED)
    
    call screen chat_interface("group")
    
    "You maintain wonderful friendships with Alex, Sam, and Riley."
    "Your group chat becomes a source of daily joy, support, and laughter."
    "Sometimes the best love stories are about the family you choose."
    
    $ endings_unlocked.append("friendship_ending")
    $ unlock_achievement("friendship_route", "Maintained all friendships")
    
    jump ending_credits

# Alone Ending
label alone_ending:
    
    scene bg chat_background
    
    "You decide to focus on yourself for now."
    "The connections you've made have taught you a lot about what you want in relationships."
    
    # Reflection
    "While you enjoyed chatting with Alex, Sam, and Riley, you realize you need time to grow as a person."
    "The friendships you've built will always be there when you're ready."
    "Sometimes the most important relationship is the one you have with yourself."
    
    $ endings_unlocked.append("alone_ending")
    $ unlock_achievement("self_discovery", "Chose the path of self-discovery")
    
    jump ending_credits

# Ending Credits
label ending_credits:
    
    scene bg phone_home
    
    "Thank you for playing Chat Novel!"
    ""
    "Your choices shaped this story and determined its outcome."
    "Each conversation mattered, each relationship grew in its own way."
    ""
    "In our digital age, real connections can happen anywhere - even through a screen."
    "What matters is the authenticity and care we bring to our interactions."
    ""
    "Statistics:"
    "Alex Relationship: [alex_relationship] points"
    "Sam Relationship: [sam_relationship] points" 
    "Riley Relationship: [riley_relationship] points"
    ""
    "Achievements Unlocked: [len(achievements)]"
    "Endings Discovered: [len(endings_unlocked)]/5"
    ""
    if len(endings_unlocked) < 5:
        "Try playing again to discover different story paths and endings!"
    else:
        "Congratulations! You've discovered all possible endings!"
    ""
    "Thank you for playing!"
    
    return

# Additional story labels for extended gameplay

# Second day conversations
label alex_day2:
    
    if not get_story_flag("alex_art_sharing"):
        return
    
    $ chat_history = []
    $ add_chat_message("alex", "Hey! I finished that art piece I mentioned", MESSAGE_RECEIVED)
    $ add_chat_message("alex", "Want to see it? I'm nervous but excited to share 😊", MESSAGE_RECEIVED)
    
    call screen chat_interface("alex")
    
    menu:
        "I'd be honored to see it!":
            $ add_chat_message(player_name, "I'd be honored to see it!", MESSAGE_SENT)
            $ add_relationship_points("alex", 5)
            $ add_chat_message("alex", "Here it is... *sends image*", MESSAGE_RECEIVED)
            $ add_chat_message("alex", "It's called 'Digital Hearts' 💕", MESSAGE_RECEIVED)
            $ set_story_flag("alex_art_seen", True)
            
        "Are you sure you're ready to share?":
            $ add_chat_message(player_name, "Are you sure you're ready to share?", MESSAGE_SENT)
            $ add_relationship_points("alex", 3)
            $ add_chat_message("alex", "You're so thoughtful... yes, I think I'm ready", MESSAGE_RECEIVED)
    
    return

label sam_day2:
    
    if not get_story_flag("sam_beta_tester"):
        return
    
    $ chat_history = []
    $ add_chat_message("sam", "The beta is ready! Here's the link", MESSAGE_RECEIVED)
    $ add_chat_message("sam", "No pressure, but I'm really curious what you think", MESSAGE_RECEIVED)
    
    call screen chat_interface("sam")
    
    menu:
        "Downloading it now!":
            $ add_chat_message(player_name, "Downloading it now!", MESSAGE_SENT)
            $ add_relationship_points("sam", 4)
            $ add_chat_message("sam", "Awesome! Let me know if you run into any bugs", MESSAGE_RECEIVED)
            $ set_story_flag("sam_app_downloaded", True)
            
        "I'll try it out this weekend":
            $ add_chat_message(player_name, "I'll try it out this weekend", MESSAGE_SENT)
            $ add_relationship_points("sam", 2)
            $ add_chat_message("sam", "Perfect! Take your time with it", MESSAGE_RECEIVED)
    
    return

label riley_day2:
    
    if not riley_online:
        $ set_character_online("riley", True)
        $ update_chat_room_info("riley", "Finally got some free time to chat", 1)
    
    $ chat_history = []
    $ add_chat_message("riley", "Finally got some free time to chat", MESSAGE_RECEIVED)
    $ add_chat_message("riley", "Studio life is consuming, but in a good way", MESSAGE_RECEIVED)
    
    call screen chat_interface("riley")
    
    menu:
        "How's the music coming along?":
            $ add_chat_message(player_name, "How's the music coming along?", MESSAGE_SENT)
            $ add_relationship_points("riley", 3)
            $ add_chat_message("riley", "Better than expected. That conversation we had really helped", MESSAGE_RECEIVED)
            
        "Don't burn yourself out":
            $ add_chat_message(player_name, "Don't burn yourself out", MESSAGE_SENT)
            $ add_relationship_points("riley", 4)
            $ add_chat_message("riley", "Thanks for caring. It means a lot", MESSAGE_RECEIVED)
    
    return

# Special events
label special_event_confession:
    
    if alex_relationship >= 25 and get_story_flag("alex_art_seen"):
        $ set_story_flag("alex_confession", True)
        jump alex_confession_scene
    
    return

label alex_confession_scene:
    
    $ chat_history = []
    $ add_chat_message("alex", "Can I tell you something important?", MESSAGE_RECEIVED)
    $ add_chat_message("alex", "I've been thinking about us a lot lately...", MESSAGE_RECEIVED)
    $ add_chat_message("alex", "I think I'm developing feelings for you 💕", MESSAGE_RECEIVED)
    
    call screen chat_interface("alex")
    
    menu:
        "I've been feeling the same way":
            $ add_chat_message(player_name, "I've been feeling the same way", MESSAGE_SENT)
            $ add_relationship_points("alex", 10)
            $ add_chat_message("alex", "Really?! This is amazing! 😍", MESSAGE_RECEIVED)
            $ set_story_flag("alex_mutual_feelings", True)
            
        "I care about you, but I need time":
            $ add_chat_message(player_name, "I care about you, but I need time", MESSAGE_SENT)
            $ add_relationship_points("alex", 2)
            $ add_chat_message("alex", "I understand. Take all the time you need", MESSAGE_RECEIVED)
            
        "I value our friendship":
            $ add_chat_message(player_name, "I value our friendship", MESSAGE_SENT)
            $ add_relationship_points("alex", -2)
            $ add_chat_message("alex", "Of course... friendship is important too", MESSAGE_RECEIVED)
    
    return

# Navigation labels for screen interactions
label phone_home_nav:
    call screen phone_home
    return

label contacts_nav:
    call screen contacts_list
    return

# Chat routing based on partner selection
label start_chat:
    
    if current_chat_partner == "alex":
        jump alex_chat
    elif current_chat_partner == "sam":
        jump sam_chat
    elif current_chat_partner == "riley":
        jump riley_chat
    elif current_chat_partner == "group":
        jump group_chat
    else:
        jump contacts_nav
    
    return

# Daily progression system
label advance_day:
    
    $ story_day += 1
    
    # Update character availability and moods
    if story_day == 2:
        $ set_character_online("riley", True)
        $ add_notification("Riley", "Riley is now online!")
    
    if story_day == 3:
        $ story_chapter = 2
        $ add_notification("Chapter 2", "New story developments await...")
    
    # Check for special events
    call special_event_confession
    
    # Progress relationship-based storylines
    if alex_relationship >= 15:
        call alex_day2
    
    if sam_relationship >= 15:
        call sam_day2
    
    if riley_relationship >= 10:
        call riley_day2
    
    return

# Achievement system integration
label check_achievements:
    
    # Relationship milestones
    if alex_relationship >= 20 and "alex_close" not in achievements:
        $ unlock_achievement("alex_close", "Became close friends with Alex")
    
    if sam_relationship >= 20 and "sam_close" not in achievements:
        $ unlock_achievement("sam_close", "Became close friends with Sam")
    
    if riley_relationship >= 20 and "riley_close" not in achievements:
        $ unlock_achievement("riley_close", "Became close friends with Riley")
    
    # Story milestones
    if get_story_flag("first_group_chat") and "social_butterfly" not in achievements:
        $ unlock_achievement("social_butterfly", "Participated in group chat")
    
    # Conversation milestones
    if len(chat_history) >= 50 and "chatterbox" not in achievements:
        $ unlock_achievement("chatterbox", "Sent 50 messages")
    
    return

# Save/Load integration
label before_save:
    # Store current state
    $ persistent.current_relationships = {
        "alex": alex_relationship,
        "sam": sam_relationship, 
        "riley": riley_relationship
    }
    $ persistent.story_progress = {
        "day": story_day,
        "chapter": story_chapter,
        "flags": story_flags
    }
    return

label after_load:
    # Restore state if available
    if persistent.current_relationships:
        $ alex_relationship = persistent.current_relationships.get("alex", 0)
        $ sam_relationship = persistent.current_relationships.get("sam", 0)
        $ riley_relationship = persistent.current_relationships.get("riley", 0)
    
    if persistent.story_progress:
        $ story_day = persistent.story_progress.get("day", 1)
        $ story_chapter = persistent.story_progress.get("chapter", 1)
        $ story_flags.update(persistent.story_progress.get("flags", {}))
    
    return
