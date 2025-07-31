# Reversi (Othello) Game with AI

This project is a Python-based implementation of the classic board game Reversi (also known as Othello). It features a graphical interface, AI opponents, and custom game logic.

## Features

- **Game Logic**: Implements the rules and mechanics of Reversi, including move validation and win conditions.
- **AI Opponent**: Play against an AI powered by neural networks and game tree algorithms.
- **Graphical Interface**: Built using `pygame` for an interactive and visually appealing experience.
- **Custom Data Structures**: Includes a custom heap implementation for efficient AI decision-making.
- **Testing**: Unit tests ensure the reliability of the game tree logic.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd Reversi-py
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the main game file to start the game:
   ```bash
   python main_game.py
   ```
2. Play against the AI or another player on the same machine.

## File Overview

- `main_game.py`: Entry point for the game.
- `game_engine.py`: Core game logic.
- `nn_ai.py`: Neural network-based AI.
- `game_tree.py`: Game tree logic for AI decision-making.
- `own_heap.py`: Custom heap implementation.
- `test_game_tree.py`: Unit tests for the game tree.
- `trained_reversi_model.pth`: Pre-trained model for the AI.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.