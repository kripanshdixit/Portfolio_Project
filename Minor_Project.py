# Function to display the Tic Tac Toe board
def display_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)


# Function for player move
def player_move(board, player):
    valid_move = False
    while not valid_move:
        move = input(f"Player {player}, enter your move (row col): ")
        try:
            row, col = map(int, move.split())
            if board[row][col] == " ":
                board[row][col] = player
                valid_move = True
            else:
                print("That cell is already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column numbers separated by a space.")
            continue


# Function to check if any player has won
def check_victory(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


# Function to check for a draw
def check_draw(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))


# Main function to run the game
def tic_tac_toe():
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        display_board(board)
        player = players[turn % 2]
        player_move(board, player)
        if check_victory(board, player):
            display_board(board)
            print(f"Player {player} wins!")
            break
        if check_draw(board):
            display_board(board)
            print("It's a draw!")
            break
        turn += 1


# Run the game
if __name__ == "__main__":
    tic_tac_toe()




def greet(name):
    return f"Hello, {name}!"
print(greet("world")) 