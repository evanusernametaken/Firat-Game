This repository contains Stray Cats, a fast-paced 2D endless-runner game built with Python and Pygame. The player controls a flying cat as it moves through a scrolling world filled with obstacles. The game features animations, procedural obstacle generation, parallax backgrounds, score tracking, and a full start-menu and death-screen flow. Player progress is recorded, and the game automatically keeps track of the highest distance achieved.

The game world scrolls continuously, displaying a layered background composed of a moving sky, distant clouds, and a looping grass floor. As the player advances, obstacles spawn at varying intervals depending on the distance traveled. These include scratching posts, yarn balls, falling objects, and special enemy types that telegraph before attacking. Each obstacle moves across the screen and interacts with the cat’s position, making timing and movement critical.

The cat's movement is controlled with simple inputs. The player can move up, left, or right, and the cat’s velocity is affected by gravity and drag. Different animations play depending on whether the cat is flying normally, flying upward, or in the death state. When the cat collides with an obstacle or hits the ground, it enters the death sequence, spins, and falls before transitioning to the death screen. At that point, the player's distance is compared with the stored high score, and if a new record is reached, it is saved automatically.

The game begins on a main menu featuring animated UI elements. From there, the player can start the game by pressing any key. During gameplay, the current distance traveled is displayed on-screen, providing constant feedback. After the cat is defeated, the death screen appears, showing the player's distance and the current high score. The game then returns to a restartable state so the player can continue playing.

Obstacle behavior is varied to keep the gameplay challenging. Some obstacles move horizontally, some bounce or fall, and others change behavior depending on how close they are to the cat. Special telegraphed enemies appear at higher distances and require the player to anticipate incoming attacks. As the distance increases, the number, frequency, and type of obstacles escalate, creating natural difficulty progression.

For clarity, the overall game structure includes:
- A main menu where the player begins.
- A start screen that transitions into the main game.
- The primary gameplay loop with procedural obstacle spawning.
- A death sequence followed by a death screen displaying scores.
- Persistent score saving using a JSON file.

To run the game, ensure that Python, Pygame, and the required asset files are installed. Launch the script in any Python environment that supports graphical output, and the game will start immediately with the main menu.
