## Test file to verify project functionality
## This file can be deleted - it's just for testing

# Test label to verify the project loads correctly
label test_project:
    "This is a test to verify the Chat Novel project is working correctly."
    "If you can see this message, the basic project structure is functional."
    "You can delete the test_project.rpy file once you've confirmed everything works."
    return

# Test the character definitions
label test_characters:
    "Testing character definitions..."
    alex "Hi! I'm Alex, the art student."
    sam "Hey there! I'm Sam, the developer."
    riley "Hello, I'm Riley, the musician."
    "Character definitions are working correctly!"
    return

# Test the phone interface
label test_phone:
    "Testing phone interface..."
    $ add_notification("Test", "This is a test notification")
    $ add_chat_message("alex", "This is a test message", MESSAGE_RECEIVED)
    "Phone interface functions are loaded correctly!"
    return
