import heapq

class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.g = float('inf')  # Cost from start node
        self.h = 0  # Heuristic (estimated cost to goal)
        self.f = 0  # Total cost: f = g + h
        self.parent = None

    def __lt__(self, other):
        return self.f < other.f

def heuristic(node, goal):
    return abs(node.row - goal.row) + abs(node.col - goal.col)

def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_list = []
    closed_set = set()

    start_node = Node(start[0], start[1])
    goal_node = Node(goal[0], goal[1])

    start_node.g = 0
    start_node.h = heuristic(start_node, goal_node)
    start_node.f = start_node.g + start_node.h

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        if current_node.row == goal_node.row and current_node.col == goal_node.col:
            path = []
            while current_node:
                path.append((current_node.row, current_node.col))
                current_node = current_node.parent
            return path[::-1]  # Reverse the path to start from the start node

        closed_set.add((current_node.row, current_node.col))

        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
        for dr, dc in neighbors:
            neighbor_row, neighbor_col = current_node.row + dr, current_node.col + dc

            if (
                0 <= neighbor_row < rows
                and 0 <= neighbor_col < cols
                and grid[neighbor_row][neighbor_col] != 1
                and (neighbor_row, neighbor_col) not in closed_set
            ):
                neighbor_node = Node(neighbor_row, neighbor_col)
                tentative_g = current_node.g + 1  # Cost to move to the neighbor is always 1

                if tentative_g < neighbor_node.g:
                    neighbor_node.parent = current_node
                    neighbor_node.g = tentative_g
                    neighbor_node.h = heuristic(neighbor_node, goal_node)
                    neighbor_node.f = neighbor_node.g + neighbor_node.h

                    if (neighbor_node.row, neighbor_node.col) not in [
                        (node.row, node.col) for node in open_list
                    ]:
                        heapq.heappush(open_list, neighbor_node)

    return None  # No path found

# Example usage:
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
]

start = (0, 0)
goal = (4, 4)

path = a_star(grid, start, goal)

if path:
    print("Shortest path:", path)
else:
    print("No path found")
