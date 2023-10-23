from classes.Node import Node
from queue import Queue
from classes.RushHourPuzzle import RushHourPuzzle
import heapq


class Search:

    """A* using the manhattan distance"""

    @staticmethod
    def astar(puzzle: RushHourPuzzle, heuristic=1):
        start_node = Node(puzzle, None, None, 0, heuristic)

        open_list: list[Node] = []

        complexity = 0

        # priority queue for the nodes to be expanded
        heapq.heappush(open_list, start_node)

        # set of nodes that have been expanded
        closed_set = set()

        while open_list:
            current_node = heapq.heappop(open_list)

            if current_node.state.isGoal():
                return current_node, complexity

            closed_set.add(current_node.state)

            successors = current_node.state.successorFunction()

            complexity += 1

            for action, successor_state in successors:
                new_node = Node(successor_state, current_node, action)

                existing_node = None
                if new_node in open_list:
                    existing_node = new_node

                if existing_node is None or new_node.f < existing_node.f:
                    if existing_node:
                        open_list.remove(existing_node)

                    heapq.heappush(open_list, new_node)

        return None

    """Uninformed/Blind Search"""

    @staticmethod
    def breadthFirst(initial_state):
        initial_node = Node(initial_state)
        # Check if the start element is the goal
        if initial_node.state.isGoal():
            return initial_node, 0

        # Create the OPEN FIFO queue and the CLOSED list
        open = Queue()  # A FIFO queue
        open.put(initial_node)
        closed = list()

        step = 0
        while True:
            print(f"*** Step {step} ***")
            # Check if the OPEN queue is empty => goal not found
            if open.empty():
                return None, step
            # Get the first element of the OPEN queue
            current = open.get()
            # Put the current node in the CLOSED list
            closed.append(current)
            step += 1
            # Generate the successors of the current node
            for action, successor in current.state.successorFunction():
                child = Node(successor, current, action)
                # Check if the child is not in the OPEN queue and the CLOSED list
                if child.state.board not in [
                    node.state.board for node in closed
                ] and child.state.board not in [
                    node.state.board for node in list(open.queue)
                ]:
                    # Check if the child is the goal
                    if child.state.isGoal():
                        print("Goal reached")
                        return child, step
                    # Put the child in the OPEN queue
                    open.put(child)

