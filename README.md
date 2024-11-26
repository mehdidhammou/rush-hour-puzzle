# Rush Hour Puzzle Solver

This project is a Rush Hour puzzle solver implemented in Python. It uses the A\* search algorithm to find the solution to the puzzle and visualizes the solution using Pygame.

## Project Structure

```
.gitignore
classes/
    Game.py
    Node.py
    RushHourPuzzle.py
    Search.py
    TestGame.py
lib/
    puzzles/
        1.csv
        2-a.csv
        2-b.csv
        2-c.csv
        2-d.csv
        2-e.csv
        2-f.csv
main.py
README.md
```

### Files and Directories

- **`Game.py`**: Handles the visualization of the puzzle using Pygame.
- **`Node.py`**: Defines the node class used in the A\* search algorithm.
- **`RushHourPuzzle.py`**: Defines the `RushHourPuzzle` class, which represents the puzzle board and its state.
- **`Search.py`**: Implements the A\* search algorithm.
- **`TestGame.py`**: Contains a test class to run the puzzle solver and visualize the solution.
- **`puzzles/`**: Contains CSV files representing different puzzle configurations.
- **`main.py`**: The main entry point of the project, initializing the puzzle, running the solver, and visualizing the solution.

## Requirements

- Python 3.x
- Pygame

## Installation

1. Clone the repository:

   ```sh
   git clone <repository-url>
   cd rush-hour-puzzle
   ```

2. Install the required packages:
   ```sh
   pip install pygame
   ```

## Usage

To run the puzzle solver and visualize the solution, execute the `main.py` script:

```sh
python main.py
```

The script will load the puzzle from the specified CSV file, solve it using the A\* search algorithm, and display the solution using Pygame.

## Puzzle Files

Puzzle files are located in the `puzzles` directory. Each file is a CSV representing a different puzzle configuration. The first line contains the board dimensions, and the subsequent lines define the vehicles and walls.

## Example

Here is an example of a puzzle file (`1.csv`):

```
6,6
A,0,0,H,2
B,0,1,V,3
#,2,2
X,3,3,H,2
```

- The first line `6,6` specifies a 6x6 board.
- The second line `A,0,0,H,2` defines a horizontal vehicle `A` at position `(0,0)` with length `2`.
- The third line `B,0,1,V,3` defines a vertical vehicle `B` at position `(0,1)` with length `3`.
- The fourth line `#,2,2` defines a wall at position `(2,2)`.
- The fifth line `X,3,3,H,2` defines a horizontal target vehicle `X` at position `(3,3)` with length `2` (There should be only one target vehicle).

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- Pygame for providing the game development library.
- The A\* search algorithm for solving the puzzle efficiently.
- Ahmed Belloula for his coding skills and fast delivery.
- Mahdi Dadi Hammou for his clean code principles and attention to detail.
