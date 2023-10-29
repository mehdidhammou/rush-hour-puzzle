from classes.RushHourPuzzle import RushHourPuzzle
from classes.Search import Search
from classes.Game import Game

PUZZLE_FILE = "lib/puzzles/1.csv"
HEURISTIC = 4

def main():
    initial_state = RushHourPuzzle(PUZZLE_FILE)
    RushHourPuzzle.printRushHourBoard(initial_state.board)
    results = Search.astar(initial_state, HEURISTIC)
    
    if results is None:
        print("No solution found")
        return
    
    goal_node, complexity = results
    
    solution = goal_node.getSolution()
    path = goal_node.getPath()
    
    print(f"Path cost: {goal_node.g}")
    print(f"Number of steps: {complexity}")
    print("Moves: {}".format(" ".join(map(str, solution))))
    

    game = Game(path, initial_state)
    game.run()    

if __name__ == "__main__":
    main()
