# Game of Nim

## About

The Game of Nim is a mathematical strategy game where players take turns removing objects from heaps. The player forced to remove the last object loses. This project extends the classic Game of Nim with the following enhancements:

1. **Advanced AI**: Using nimbers (Grundy numbers) and the Minimax algorithm with Alpha-Beta pruning, the AI plays optimally in all scenarios.
2. **Graphical User Interface (GUI)**: Developed with Pygame, the GUI provides a dynamic and interactive gameplay experience, complete with animations and user feedback.
3. **Custom Features**: The game accommodates multiple rows of heaps, increasing the strategic complexity, and offers engaging gameplay for players of all skill levels.

## Setup Instructions

1. **Create a Virtual Environment**

   - Open your terminal or command prompt.
   - Navigate to the directory containing your project.
   - Run the following command to create a virtual environment:
     ```bash
     python3 -m venv venv
     ```
   - This will create a folder named `venv` in your project directory that contains the virtual environment.

2. **Activate the Virtual Environment**

   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```cmd
     venv\Scripts\activate
     ```
   - You should now see `(venv)` at the beginning of your command line, indicating the environment is active.

3. **Install Dependencies**

   - With the virtual environment activated, install the required packages by running:
     ```bash
     pip install -r requirements.txt
     ```
   - This command installs all packages listed in `requirements.txt`.

4. **Run the Game of Nim**

   - Start the game by running the main Python script:
     ```bash
     python main.py
     ```
   - Enjoy playing against the AI or another human player!

5. **Deactivate the Virtual Environment**
   - When you’re done, you can deactivate the virtual environment by running:
     ```bash
     deactivate
     ```

## Features

- **Optimal AI**: Leveraging advanced mathematical strategies, the AI provides a challenging opponent.
- **Interactive GUI**: Visualizes game states dynamically, making it accessible and enjoyable for all players.
- **Enhanced Gameplay**: Multiple rows of heaps and support for more complex game states add depth to the classic game.

## Future Work

- Add difficulty scaling to make the AI suitable for all skill levels.
- Develop a tutorial mode to teach players the rules and optimal strategies.
- Introduce networked multiplayer for remote competitive gameplay.

## References

- [Pygame Documentation](https://www.pygame.org/docs/)
- [Grundy Number (Wikipedia)](https://en.wikipedia.org/wiki/Grundy_number)
- [The Game of Nim (Wikipedia)](https://en.wikipedia.org/wiki/Nim)
