from copy import deepcopy
import csv


class RushHourPuzzle:
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, RushHourPuzzle):
            return self.board == __value.board
        return False

    def __hash__(self) -> int:
        return hash(tuple(map(tuple, self.board)))

    def __init__(self, puzzle_file):
        # Initialize the RushHourPuzzle Board
        self.setVehicles(puzzle_file)
        self.setBoard()

    def setVehicles(self, puzzle_file):
        # Open file
        with open(puzzle_file) as file:
            # Create reader object by passing the file
            # object to reader method
            csvreader = csv.reader(file)
            w, h = next(csvreader)
            self.board_width, self.board_height = int(w), int(h)
            self.vehicles = []
            self.walls = []
            for line in csvreader:
                if line[0] == "#":
                    self.walls.append((int(line[1]), int(line[2])))
                else:
                    id, x, y, orientation, length = line
                    vehicle = {
                        "id": id,
                        "x": int(x),
                        "y": int(y),
                        "orientation": orientation,
                        "length": int(length),
                    }
                    self.vehicles.append(vehicle)

    def setBoard(self):
        self.board = [
            [" " for _ in range(self.board_width)] for _ in range(self.board_height)
        ]
        for x, y in self.walls:
            self.board[y][x] = "#"
        for vehicle in self.vehicles:
            x, y = vehicle["x"], vehicle["y"]
            if vehicle["orientation"] == "H":
                for i in range(vehicle["length"]):
                    self.board[y][x + i] = vehicle["id"]
            else:
                for i in range(vehicle["length"]):
                    self.board[y + i][x] = vehicle["id"]

    @staticmethod
    def printRushHourBoard(board):
        for row in board:
            print(" | ".join(map(str, row)))
            print("----------------------")

    # check if the red car is at the winning position
    def isGoal(self):
        for vehicle in self.vehicles:
            if vehicle["id"] == "X" and vehicle["x"] == self.board_width - 2:
                return True
        return False

    # Generate the successors
    def successorFunction(self) -> list[tuple[str, "RushHourPuzzle"]]:
        succs = list()
        for index, vehicle in enumerate(self.vehicles):
            x_position = vehicle["x"]
            y_position = vehicle["y"]

            # check if vehicle is oriented horizontally
            if vehicle["orientation"] == "H":
                # move left if it's not on the edge of the board and it's not blocked by another vehicle
                if x_position > 0 and self.board[y_position][x_position - 1] == " ":
                    successor = deepcopy(self)
                    successor.vehicles = deepcopy(self.vehicles)
                    # update the vehicle's position
                    successor.vehicles[index]["x"] = x_position - 1
                    # update the board
                    successor.setBoard()
                    succs.append(("{}:L".format(vehicle["id"]), successor))

                # move right if it's not on the edge of the board and it's not blocked by another vehicle
                if (
                    x_position + vehicle["length"] < self.board_width
                    and self.board[y_position][x_position + vehicle["length"]] == " "
                ):
                    successor = deepcopy(self)
                    successor.vehicles = deepcopy(self.vehicles)
                    # update the vehicle's position
                    successor.vehicles[index]["x"] = x_position + 1
                    # update the board
                    successor.setBoard()
                    succs.append(("{}:R".format(vehicle["id"]), successor))

            else:
                # move up if it's not on the edge of the board and it's not blocked by another vehicle
                if y_position > 0 and self.board[y_position - 1][x_position] == " ":
                    successor = deepcopy(self)
                    successor.vehicles = deepcopy(self.vehicles)
                    # update the vehicle's position
                    successor.vehicles[index]["y"] = y_position - 1
                    # update the board
                    successor.setBoard()
                    succs.append(("{}:U".format(vehicle["id"]), successor))

                # move down if it's not on the edge of the board and it's not blocked by another vehicle
                if (
                    y_position + vehicle["length"] < self.board_height
                    and self.board[y_position + vehicle["length"]][x_position] == " "
                ):
                    successor = deepcopy(self)
                    successor.vehicles = deepcopy(self.vehicles)
                    # update the vehicle's position
                    successor.vehicles[index]["y"] = y_position + 1
                    # update the board
                    successor.setBoard()
                    succs.append(("{}:D".format(vehicle["id"]), successor))
        return succs
