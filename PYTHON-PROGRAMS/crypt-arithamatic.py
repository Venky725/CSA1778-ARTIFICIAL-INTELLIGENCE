def is_valid_assignment(letters, assignment):
    return all(assignment[letter] != 0 for letter in letters)


def solve_cryptarithmetic(letters, puzzle, assignment, carry, index):
    if index == len(puzzle):
        return carry == 0

    current_letter = puzzle[index]

    if current_letter in assignment:
        return solve_cryptarithmetic(letters, puzzle, assignment, carry, index + 1)

    for digit in range(10):
        if digit not in assignment.values():
            assignment[current_letter] = digit
            if is_valid_assignment(letters, assignment):
                next_carry = carry
                if current_letter in letters:
                    next_carry, _ = divmod(assignment[current_letter] + carry, 10)
                if solve_cryptarithmetic(letters, puzzle, assignment, next_carry, index + 1):
                    return True
            assignment[current_letter] = None

    return False


def solve_cryptarithmetic_problem(puzzle):
    words = puzzle.split()[:-2]
    letters = set("".join(words))
  #  letters_no_zero = set(words[0])
    # ...

    letters_no_zero = set(words[0])
    letters_no_zero_copy = set(letters_no_zero)  # Create a copy of the set
    for letter in letters_no_zero_copy:
        letters_no_zero.add(letter.upper())

    # Check if each word has at most one letter that is not in the other words
    for i in range(len(words)):
        other_words = words[:i] + words[i + 1:]
        for letter in letters:
            if letter not in other_words and words[i].count(letter) > 1:
                return None

    assignment = {}
    if solve_cryptarithmetic(letters_no_zero, puzzle, assignment, 0, 0):
        return assignment
    else:
        return None


# Example usage:
puzzle = "send + more = money"
solution = solve_cryptarithmetic_problem(puzzle)

if solution:
    print("Solution:")
    for letter, digit in solution.items():
        print(f"{letter}: {digit}")
else:
    print("No solution found.")
