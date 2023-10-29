from __future__ import annotations
from classes.RushHourPuzzle import RushHourPuzzle


class Node:
    def __hash__(self) -> int:
        return hash(self.state)

    def __eq__(self, other):
        if not isinstance(other, Node):
            return NotImplemented
        return self.state == other.state

    def __lt__(self, other):
        return self.f < other.f

    def __init__(
        self, state: RushHourPuzzle, parent: Node = None, action="", c=1, heuristic=1
    ):
        self.state = state
        self.parent = parent
        self.action = action
        self.g = 0 if not self.parent else self.parent.g + c
        self.f = self.setF(heuristic)

    # Choose one of the available heuristics
    def setF(self, heuristic) -> int:
        heuristics = {
            1: lambda: self.heuristic1(),
            2: lambda: self.heuristic2(),
            3: lambda: self.heuristic3(),
            4: lambda: (self.heuristic1() + self.heuristic2()) ** 3,
        }
        return self.g + heuristics[heuristic]()

    """ First heuristic: Distance from target vehicle to the exit """

    def heuristic1(self):
        for vehicle in self.state.vehicles:
            if vehicle["id"] == "X":
                return self.state.board_width - 2 - vehicle["x"]

    """ Second heuristic: number of vehicles that block the way to the exit """
    # def heuristic2(self):
        #     for vehicle in self.state.vehicles:
        #         if vehicle["id"] == "X":
        #             unique_vehicles = set(self.state.board[vehicle["y"]][vehicle["x"] :])
        #             if " " in unique_vehicles:
        #                 return self.heuristic1() + len(unique_vehicles) - 2
        #             return self.heuristic1() + len(unique_vehicles) - 1
   
            
    def heuristic2(self):
    #    write another heuristic that is admissible and consistent
        count = 0
        for vehicle in self.state.vehicles:
            if vehicle["id"] == "X":
                for i in range(vehicle["x"] + vehicle["length"], self.state.board_width):
                    if self.state.board[vehicle["y"]][i] != ".":
                        count += 1
                return count
            
        


    """ Third heuristic: manhattan distance from target vehicle to the exit """

    def heuristic3(self):
        for vehicle in self.state.vehicles:
            if vehicle["id"] == "X":
                return (
                    self.state.board_width
                    - 2
                    - vehicle["x"]
                    + abs(self.state.board_height // 2 - 1 - vehicle["y"])
                )

    def getPath(self) -> list[RushHourPuzzle]:
        states = []
        node = self
        while node != None:
            states.append(node.state)
            node = node.parent
        return states[::-1]

    def getSolution(self) -> list[str]:
        actions = []
        node = self
        while node != None:
            actions.append(node.action)
            node = node.parent
        return actions[::-1]
