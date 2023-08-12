class State:
    def __init__(self, missionaries, cannibals, boat):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
        self.parent = None

    def is_valid(self):
        if self.missionaries < 0 or self.cannibals < 0:
            return False
        if self.missionaries > 3 or self.cannibals > 3:
            return False
        if (self.missionaries < self.cannibals) and self.missionaries > 0:
            return False
        if (3 - self.missionaries < 3 - self.cannibals) and (3 - self.missionaries > 0):
            return False
        return True

    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0 and self.boat == 0

    def __eq__(self, other):
        return self.missionaries == other.missionaries and \
               self.cannibals == other.cannibals and \
               self.boat == other.boat

    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat))

    def __str__(self):
        return f"({self.missionaries}, {self.cannibals}, {self.boat})"


def successors(state):
    succ = []
    if state.boat == 0:
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:
                    new_state = State(state.missionaries - m, state.cannibals - c, 1)
                    if new_state.is_valid():
                        new_state.parent = state
                        succ.append(new_state)
    else:
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:
                    new_state = State(state.missionaries + m, state.cannibals + c, 0)
                    if new_state.is_valid():
                        new_state.parent = state
                        succ.append(new_state)
    return succ


def dfs(initial_state):
    visited = set()
    stack = [initial_state]

    while stack:
        current_state = stack.pop()
        if current_state.is_goal():
            return current_state
        visited.add(current_state)

        for successor in successors(current_state):
            if successor not in visited and successor not in stack:
                stack.append(successor)

    return None


def print_solution(solution):
    path = []
    current_state = solution
    while current_state:
        path.append(current_state)
        current_state = current_state.parent

    path.reverse()
    for state in path:
        print(state)


initial_state = State(3, 3, 1)
solution = dfs(initial_state)

if solution:
    print("Solution found:")
    print_solution(solution)
else:
    print("No solution found.")
