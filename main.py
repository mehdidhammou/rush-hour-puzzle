from classes.RushHourPuzzle import RushHourPuzzle
from classes.Search import Search
from classes.Game import Game
from classes.TestGame import TestGame
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
    
    print(f"Path cost: {goal_node.g}")
    print(f"Number of steps: {complexity}")
    print("Moves: {}".format(" ".join(map(str, solution))))
    
    path = goal_node.getPath()
    game = Game(path, initial_state)
    game.run()    

def main2():
    initial_state = RushHourPuzzle(PUZZLE_FILE)
    RushHourPuzzle.printRushHourBoard(initial_state.board)
    TestGame.run(initial_state, HEURISTIC)
    
    
main2()