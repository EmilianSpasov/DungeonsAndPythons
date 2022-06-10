# DungeonsAndPythons

Python console application, which represents a simplified verions of the original game "Dungeons & Dragons". The application is build entirely using OOP and its good practices and principles.

# Realization
The game is divided into a few components - dungeon, entities, items, utils, resources and tests.
- Dungeon - contains all the 'business' logic - how everything interacts with the map and what happens at each move and at any position of the map.
- Entities - all of the 'characters' in the game - heroes, villians etc.
- Items - all of the usable objects in the game - weapons, spells etc.
- Resources - all of the static content for the application - .txt files, constants etc.
- Tests - unit and component tests of the more important pieces of the code.

# Goal of the game and gameplay
How to play the game:

1.Use arrow keys or W, A, S, D buttons to move your character on the map

2.Use special commands to view information:

- 'h' - will display the help message
- 'c' - will display info about your character
- 'k' - will display map keys
- 'l' - will display dungeon lore
- 'p' - will display credits
- 'q' - quit

The goal of the game is to reach the exit of the dungeon. (More information [here](resources/files/intro.txt))


# Tests and CI/CD
I added a bunch of tests to assure the best functionality of the application. Also created a small CI/CD with GitHub actions for automated testing (no deployment for now).