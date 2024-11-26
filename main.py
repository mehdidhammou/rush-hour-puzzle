from classes.RushHourPuzzle import RushHourPuzzle
from classes.Search import Search
from classes.Game import Game
from classes.TestGame import TestGame
import os

PUZZLE_FILE = "1.csv"
PUZZLE_FILE_PATH = os.path.join(
    os.path.dirname(__file__), "lib", "puzzles", PUZZLE_FILE
)
HEURISTIC = 4


def run_without_display():
    initial_state = RushHourPuzzle(PUZZLE_FILE_PATH)
    RushHourPuzzle.printRushHourBoard(initial_state.board)
    results = Search.astar(initial_state, HEURISTIC)

    if results is None:
        print("No solution found")
        return

    goal_node, complexity = results

    solution = goal_node.getSolution()

    print(f"Path cost: {goal_node.g}")
    print(f"Number of steps: {complexity}")
    print("Moves: {}".format(" ".join(map(str, solution))))

    path = goal_node.getPath()
    game = Game(path, initial_state)
    game.run()


def run_with_display():
    initial_state = RushHourPuzzle(PUZZLE_FILE_PATH)
    RushHourPuzzle.printRushHourBoard(initial_state.board)
    res = TestGame.run(initial_state, HEURISTIC)

    if res is None:
        print("No solution found")
        return

    goal_node, complexity = res

    solution = goal_node.getSolution()

    print(f"Path cost: {goal_node.g}")
    print(f"Number of steps: {complexity}")
    print("Moves: {}".format(" ".join(map(str, solution))))

    path = goal_node.getPath()
    game = Game(path, initial_state)
    game.run()


if __name__ == "__main__":

    # Without display is faster, but only prints the solution
    # run_without_display()

    # With display is slower, but shows all tree nodes and moves
    run_with_display()
