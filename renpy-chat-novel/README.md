# Chat Novel - Ren'Py Visual Novel Game

A chat-based visual novel game built for Ren'Py with a 720x1280 portrait resolution, designed to simulate a mobile messaging experience.

## Game Overview

Chat Novel is an interactive visual novel that takes place entirely through a simulated phone interface. Players interact with three main characters through text messages, building relationships and making choices that affect the story outcome.

### Characters

- **Alex Chen** (22) - Art Student
  - Creative and passionate about digital art
  - Loves deep conversations about life and dreams
  - Relationship path: Romance/Friendship

- **Sam Rodriguez** (24) - Software Developer  
  - Tech enthusiast who loves coding and gaming
  - Has a dry sense of humor and enjoys philosophical debates
  - Relationship path: Partnership/Friendship

- **Riley Park** (21) - Music Producer
  - Aspiring musician with a love for indie rock and electronic beats
  - Often busy with studio sessions, more reserved
  - Relationship path: Romance/Friendship

### Features

- **Mobile-First Design**: 720x1280 resolution optimized for portrait orientation
- **Realistic Chat Interface**: Authentic messaging app experience with:
  - Chat bubbles for sent/received messages
  - Typing indicators
  - Online/offline status
  - Message timestamps
  - Contact list with avatars
- **Branching Storylines**: Multiple conversation paths and endings
- **Relationship System**: Build relationships through meaningful conversations
- **Achievement System**: Unlock achievements for story milestones
- **Multiple Endings**: 5 different endings based on player choices
- **Save/Load System**: Full save game support with relationship tracking

### Story Structure

- **Day 1**: Introduction and first conversations
- **Day 2**: Deeper character development and relationship building
- **Day 3+**: Advanced storylines and ending paths

### Endings Available

1. **Alex Ending**: Romance path with the artist
2. **Sam Ending**: Partnership path with the developer
3. **Riley Ending**: Romance path with the musician
4. **Friendship Ending**: Maintain friendships with all characters
5. **Alone Ending**: Focus on self-discovery

## Technical Requirements

### Ren'Py Version
- Ren'Py 8.0+ recommended
- Compatible with Ren'Py 7.4+

### Resolution
- **Screen Size**: 720x1280 (portrait)
- **Aspect Ratio**: 9:16
- **Target Platform**: Mobile-friendly, also works on desktop

### File Structure

```
renpy-chat-novel/
├── project.json                 # Project configuration
├── game/
│   ├── options.rpy             # Game options and configuration
│   ├── gui.rpy                 # GUI styles and definitions
│   ├── characters.rpy          # Character definitions and functions
│   ├── screens.rpy             # Custom screen definitions
│   ├── script.rpy              # Main story script
│   ├── images/
│   │   ├── backgrounds/        # Background images
│   │   ├── characters/         # Character sprites
│   │   ├── avatars/           # Character avatars for chat
│   │   └── ui/                # UI elements
│   └── audio/
│       ├── music/             # Background music
│       └── sfx/               # Sound effects
└── README.md                   # This file
```

## Installation & Setup

### For Players
1. Install Ren'Py from https://www.renpy.org/
2. Download or clone this project
3. Open Ren'Py Launcher
4. Click "Add Existing Project" and select the `renpy-chat-novel` folder
5. Click "Launch Project" to play

### For Developers
1. Clone this repository
2. Open in Ren'Py Launcher for testing
3. Add your own images to the `game/images/` directories
4. Add audio files to the `game/audio/` directories
5. Customize the story in `script.rpy`

## Customization

### Adding Images
- Replace placeholder README files in image directories with actual PNG files
- Character sprites: 400x600px recommended
- Avatars: 80x80px circular
- Backgrounds: 720x1280px

### Adding Audio
- Music: OGG format, 44.1kHz stereo
- SFX: OGG format, 44.1kHz mono/stereo, short duration
- Place files in appropriate audio subdirectories

### Modifying Story
- Edit `script.rpy` for main story content
- Modify `characters.rpy` for character definitions
- Customize `screens.rpy` for UI changes
- Adjust `options.rpy` for game settings

## Gameplay Instructions

1. **Start**: Enter your name when prompted
2. **Navigation**: Use the phone interface to navigate between apps
3. **Messaging**: Click on contacts to start conversations
4. **Choices**: Select dialogue options to shape relationships
5. **Progress**: Continue conversations to unlock new story content
6. **Endings**: Reach different endings based on your relationship choices

## Development Notes

### Key Features Implemented
- ✅ Mobile-optimized 720x1280 resolution
- ✅ Realistic chat interface with bubbles and timestamps
- ✅ Character relationship tracking system
- ✅ Multiple branching storylines
- ✅ Achievement system
- ✅ Save/load functionality
- ✅ Multiple endings (5 total)
- ✅ Typing indicators and online status
- ✅ Group chat functionality
- ✅ Phone-like UI with apps and notifications

### Future Enhancements
- [ ] Add actual image assets
- [ ] Include background music and sound effects
- [ ] Add more characters and storylines
- [ ] Implement emoji and sticker system
- [ ] Add photo sharing in chats
- [ ] Create animated typing indicators
- [ ] Add voice message simulation

## Credits

Created as a Ren'Py visual novel template for chat-based storytelling.

### Technologies Used
- **Ren'Py**: Visual novel engine
- **Python**: Scripting language
- **Custom CSS-like styling**: For chat interface design

## License

This project is provided as a template for educational and creative purposes. Feel free to modify and use for your own visual novel projects.

---

**Note**: This is a complete, playable Ren'Py project. While it includes placeholder assets, the game logic, story, and interface are fully functional. Add your own images and audio to create a polished final product.
