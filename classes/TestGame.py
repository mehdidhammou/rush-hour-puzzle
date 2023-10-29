import pygame
from classes.RushHourPuzzle import RushHourPuzzle
from classes.Node import Node
import heapq


class TestGame:

    @staticmethod
    def run(puzzle, heuristic):
        # Initialize Pygame

        start_node = Node(puzzle, None, None, 0, heuristic)

        open_list: list[Node] = []

        complexity = 0

        # priority queue for the nodes to be expanded
        heapq.heappush(open_list, start_node)

        # set of nodes that have been expanded
        closed_set = set()
        pygame.init()

        clock = pygame.time.Clock()

        # define colors
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        WALL_COLOR = (125, 125, 125)
        BOARD_COLOR = (200, 200, 200)  # Gray for the board background
        GOAL_COLOR = (0, 128, 128)  # Green for the goal location
        RED = (255, 51, 51)
        BLUE = (102, 102, 204)
        PURPLE = (153, 102, 255)
        GREEN = (102, 204, 102)

        # Define the window size based on the Rush Hour puzzle dimensions
        board_width = puzzle.board_width
        board_height = puzzle.board_height
        cell_size = 80  # Adjust cell size for better visibility
        window_width = board_width * cell_size + 2 * cell_size  # Add extra for margin
        window_height = board_height * cell_size + 2 * cell_size  # Add extra for margin

        # Margin size for row and column numbers
        margin = cell_size

        # Adjust this value for the desired border width
        border_size = 5

        # Create a Pygame window
        screen = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("Rush Hour Puzzle Visualization")

        # Define a dictionary to map vehicle lengths to colors
        length_colors = {
            2: BLUE,  # Green for 2-cell vehicles
            3: PURPLE,  # Blue for 3-cell vehicles
            # Add more colors for other lengths as needed
        }

        # Game loop for visualization
        while open_list:
            # Quit Pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            current_node = heapq.heappop(open_list)

            if current_node.state.isGoal():
                return current_node, complexity

            closed_set.add(current_node)

            successors = current_node.state.successorFunction()

            complexity += 1

            # Clear the screen
            screen.fill(WHITE)

            # Draw the outer board rectangle with a black border
            board_rect = pygame.Rect(
                margin, margin, window_width - 2 * margin, window_height - 2 * margin
            )
            pygame.draw.rect(
                screen, BOARD_COLOR, board_rect, 0
            )  # Filled rectangle with BOARD_COLOR

            # Draw the vehicles on the board with a single ID and border for non-empty cells
            for vehicle in current_node.state.vehicles:
                id, x, y, orientation, length = (
                    vehicle["id"],
                    vehicle["x"],
                    vehicle["y"],
                    vehicle["orientation"],
                    vehicle["length"],
                )

                color = length_colors.get(length, BLACK)

                if id == "X":
                    color = RED

                if orientation == "H":
                    rect = pygame.Rect(
                        x * cell_size + margin,
                        y * cell_size + margin,
                        cell_size * length,
                        cell_size,
                    )
                else:
                    rect = pygame.Rect(
                        x * cell_size + margin,
                        y * cell_size + margin,
                        cell_size,
                        cell_size * length,
                    )

                # Draw the filled vehicle rectangle
                pygame.draw.rect(screen, color, rect)

                font = pygame.font.Font(None, 36)
                text = font.render(id, True, WHITE)  # Use WHITE color for text
                text_rect = text.get_rect()
                text_rect.center = (rect.centerx, rect.centery)
                screen.blit(text, text_rect)

                # Draw the border rectangle with the board's color for non-empty cells
                if id != " ":
                    border_rect = pygame.Rect(rect.x, rect.y, rect.width, rect.height)
                    pygame.draw.rect(screen, BOARD_COLOR, border_rect, border_size)

            # Draw the walls on the board
            for wall in puzzle.walls:
                x, y = wall
                pygame.draw.rect(
                    screen,
                    WALL_COLOR,
                    (
                        (x * cell_size) + margin,
                        (y * cell_size) + margin,
                        cell_size,
                        cell_size,
                    ),
                    0,
                )
                # add border for walls with the board's color
                border_rect = pygame.Rect(
                    x * cell_size + margin, y * cell_size + margin, cell_size, cell_size
                )
                pygame.draw.rect(screen, BOARD_COLOR, border_rect, border_size)

            # Draw the goal line on the right side of the board
            goal_y = board_height // 2 - 1
            goal_x = board_width - 1  # Rightmost column
            goal_x_position = (goal_x + 1) * cell_size + margin - border_size + 2
            goal_y_position = (goal_y * cell_size) + margin + border_size
            goal_line_width = 5  # Adjust this value for the desired line width
            pygame.draw.line(
                screen,
                GOAL_COLOR,
                (goal_x_position, goal_y_position),
                (goal_x_position, goal_y_position + cell_size - 5),
                goal_line_width,
            )

            # Display row numbers
            font = pygame.font.Font(None, 36)
            for y in range(board_height):
                text = font.render(str(y), True, BLACK)
                text_rect = text.get_rect()
                text_rect.center = (
                    margin // 2,
                    margin + y * cell_size + cell_size // 2,
                )
                screen.blit(text, text_rect)

            # Display column numbers
            for x in range(board_width):
                text = font.render(str(x), True, BLACK)
                text_rect = text.get_rect()
                text_rect.center = (
                    margin + x * cell_size + cell_size // 2,
                    margin // 2,
                )
                screen.blit(text, text_rect)

            # Update the display
            pygame.display.update()

            clock.tick(60)

            for action, successor_state in successors:
                new_node = Node(successor_state, current_node, action)

                # existing_node = None

                if new_node not in open_list and new_node not in closed_set:
                    heapq.heappush(open_list, new_node)

                elif new_node in open_list:
                    for node in open_list:
                        if node == new_node and node > new_node:
                            open_list.remove(node)
                            heapq.heappush(open_list, new_node)
                            break

                elif new_node in closed_set:
                    for node in closed_set:
                        if node == new_node and node > new_node:
                            closed_set.remove(node)
                            heapq.heappush(open_list, new_node)
                            break

        pygame.quit()
        return None