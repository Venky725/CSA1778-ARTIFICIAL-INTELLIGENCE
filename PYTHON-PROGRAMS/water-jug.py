from collections import deque


def water_jug_problem(capacity_a, capacity_b, target):
    def get_neighbors(state):
        a, b = state
        neighbors = []

        # Fill jug A
        neighbors.append((capacity_a, b))

        # Fill jug B
        neighbors.append((a, capacity_b))

        # Empty jug A
        neighbors.append((0, b))

        # Empty jug B
        neighbors.append((a, 0))

        # Pour from A to B
        pour_amount = min(a, capacity_b - b)
        neighbors.append((a - pour_amount, b + pour_amount))

        # Pour from B to A
        pour_amount = min(b, capacity_a - a)
        neighbors.append((a + pour_amount, b - pour_amount))

        return neighbors

    start_state = (0, 0)
    visited = set()
    queue = deque([(start_state, [])])

    while queue:
        current_state, path = queue.popleft()

        if current_state in visited:
            continue

        visited.add(current_state)

        if current_state[0] == target or current_state[1] == target:
            return path + [current_state]

        neighbors = get_neighbors(current_state)

        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append((neighbor, path + [current_state]))

    return None


# Example usage:
capacity_a = 4
capacity_b = 3
target = 2

solution_path = water_jug_problem(capacity_a, capacity_b, target)

if solution_path:
    print("Solution Path:")
    for state in solution_path:
        print(state)
else:
    print("No solution found.")
