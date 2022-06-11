"""
Tic Tac Toe assignment
Aurthor: Oluwadamilar Daniel Obalana
"""

# Print board
# Ask user for input
# Check for winner
# Switch user
# Loop
# End game when there is a win or a tie

def main():
    while game_running == True:
        print_board(board)
        user_input(board)
        check_winner()
        check_tie(board)
        switch_player()
        end_game()

board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

current_user = "X"

winner = None

tie = None

game_running = True

def print_board(board):
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}")

def user_input(board):
    global current_user
    user = int(input(f"{current_user}'s turn to enter a square between (1- 9): "))
    if user >= 1 and user <= 9 and board[user-1] == "-":
        board[user-1] = current_user
    else:
        print("That space has been occupied") 
        user = int(input(f"{current_user}'s turn to enter a square between (1-9): "))
        if user >= 1 and user <= 9 and board[user-1] == "-":
            board[user-1] = current_user

def check_horizontally(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    if board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def check_vertically(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def check_diagonally(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def check_winner():
    global winner
    if check_diagonally(board) or check_horizontally(board) or check_vertically(board):
        print_board(board)
        print(f"The winner is {winner}")

def check_tie(board):
    global tie
    if "-" not in board:
        tie = True
        print_board(board)
        return tie
        

def switch_player():
    global current_user
    if current_user == "X":
        current_user = "O"
    else:
        current_user = "X"

def end_game():
    global game_running
    global winner
    global tie
    if winner:
        game_running = False
        return game_running
    elif tie:
        game_running = False
        print("It is a tie!")
        print("Thanks for playing")

if __name__ == "__main__":
    main()