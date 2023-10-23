from classes.RushHourPuzzle import RushHourPuzzle
from classes.Search import Search

PUZZLE_FILE = "lib/puzzles/1.csv"


def main():
    initial_state = RushHourPuzzle(PUZZLE_FILE)
    RushHourPuzzle.printRushHourBoard(initial_state.board)
    goal_node, complexity = Search.astar(initial_state, 2)
    print(f"Path cost: {goal_node.g}")
    print(f"Number of steps: {complexity}")
    print("Moves: {}".format(" ".join(map(str, goal_node.getSolution()))))


if __name__ == "__main__":
    main()
