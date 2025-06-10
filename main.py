def main():
    # initialize the game board - create a 3x3 grid initialized with empty spaces
    board = initialize_board()

    # Display game board - write a function to display the current board state
    display_board(board)

    # Capture the player input - ask current player for their move (validate input making sure chosen space is empty, if not display message of invalid move) "This position has already been taken, please try again"
    get_player_move("O", board)


# update the board - place the player's marker on chosen space
# check for a winner or a tie - check rows, columns, and diagonals for a win condition - also will check to see if the board is full and no winner exists in which case it would be a tie
# Switch player
# Game loop - repeat the above steps (except initialize) until a win or tie is reached
# End the game by annoucing winner or declaring a tie


def initialize_board():
    # return [["_", "_", "_"] for _ in range(3)]
    board = []  # holds the 3 rows
    for row_index in range(3):
        row = []  # create an empty row
        for col_index in range(3):
            row.append("_")  # this adds an empty cell to the row
        board.append(row)  # this adds the completed row to the board
    return board


def display_board(board):
    for row in board:
        print(" ".join(row))


def get_player_move(player, board):
    row = input(f"It is {player}'s turn, pick a row (1-3): ")
    column = input("Pick a column (1-3): ")
    board[int(row) - 1][int(column) - 1] = player
    display_board(board)


if __name__ == "__main__":
    main()
