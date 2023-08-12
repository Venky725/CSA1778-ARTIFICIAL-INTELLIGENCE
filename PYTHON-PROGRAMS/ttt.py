def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def get_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid move. Please choose a number between 1 and 9.")
            else:
                return divmod(move, 3)
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    for _ in range(9):
        row, col = get_move()
        if board[row][col] == ' ':
            board[row][col] = players[current_player]
            print_board(board)
            if check_winner(board, players[current_player]):
                print(f"Player {players[current_player]} wins!")
                break
            elif is_board_full(board):
                print("It's a draw!")
                break
            current_player = 1 - current_player
        else:
            print("Cell already occupied. Try again.")

if __name__ == "__main__":
    main()
