board = [[' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ']]

def printBoard(board):
    print(" 1  2  3  4  5  6  7")
    for i in range(6):
        print("[" + board[i][0] + "][" + board[i][1] + "][" + board[i][2] + "][" + board[i][3] + "][" + board[i][4] + "][" + board[i][5] + "][" + board[i][6] + "]")

def checkWin(player):
    for i in range(len(board)):
        for j in range(len(board[0])-3):
            if board[i][j] == player and board[i][j+1] == player and board[i][j+2] == player and board[i][j+3] == player:
                return True
    for j in range(len(board[0])):
        for i in range(len(board)-3):
            if board[i][j] == player and board[i+1][j] == player and board[i+2][j] == player and board[i+3][j] == player:
                return True
    for i in range(len(board[0])-3):
        for j in range(len(board)-3):
            if board[j][i] == player and board[j+1][i+1] == player and board[j+2][i+2] == player and board[j+3][i+3] == player:
                return True
    for i in range(6,2,-1):
        for j in range(len(board)-3):
            if board[j][i] == player and board[j+1][i-1] == player and board[j+2][i-2] == player and board[j+3][i-3] == player:
                return True
    return False


def playerMove(player):
    columnMove = int(input("Choose a column: ")) - 1
    if columnMove > -1 and columnMove < 7:
        if board[5][columnMove] == ' ':
            board[5][columnMove] = player
            printBoard(board)
        elif board[4][columnMove] == ' ':
            board[4][columnMove] = player
            printBoard(board)
        elif board[3][columnMove] == ' ':
            board[3][columnMove] =player
            printBoard(board)
        elif board[2][columnMove] == ' ':
            board[2][columnMove] = player
            printBoard(board)
        elif board[1][columnMove] == ' ':
            board[1][columnMove] = player
            printBoard(board)
        elif board[0][columnMove] == ' ':
            board[0][columnMove] = player
            printBoard(board)
        else:
            print("Choose a different column.")
            playerMove(player)
    else:
        print("Stay in the board.")
        playerMove(player)

def game():
    printBoard(board)
    print("Use your keypad to move. Ex. if player one selects number 7 on the keypad then their move will be in column 7")
    playerOne = input("Player one is: ").upper()
    playerTwo = input("Player two is: ").upper()
    count = 0
    for x in range(21):
        playerMove(playerOne)
        if checkWin(playerOne):
            print("Player one wins!")
            break
        if count < 42:
            playerMove(playerTwo)
            count += 1
            if checkWin(playerTwo):
                print("Player two wins!")
                break
        else:
            print("Tie")
            break

game()
