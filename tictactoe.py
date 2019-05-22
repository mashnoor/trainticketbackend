game = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


def isAnyRowMatch():
    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2] != " ":
            return True, game[i][0]
    return False


def isAnyColumnMatch():
    for i in range(3):
        if game[0][i] == game[1][i] == game[2][i] != " ":
            return True, game[0][i]

    return False


def isAnyDiagonalMatch():
    if game[0][0] == game[1][1] == game[2][2] != " ":
        return True
    elif game[0][2] == game[1][1] == game[2][0] != " ":
        return True
    else:
        return False


def whoWon():
    verdict_1 = isAnyRowMatch()
    verdict_2 = isAnyColumnMatch()
    verdict_3 = isAnyDiagonalMatch()

    if verdict_1 or verdict_2 or verdict_3:
        return True

    else:
        return False


def isDraw():
    if whoWon():
        for i in range(3):
            for j in range(3):
                if game[i][j] == "":
                    return False
        return True
    else:
        return False


def drawBoard():
    board = "|  " + game[0][0] + " |  " + game[0][1] + " |  " + game[0][2] + " |  "
    print(board)
    print(" --- " * 3)

    board = "|  " + game[1][0] + " |  " + game[1][1] + " |  " + game[1][2] + " |  "
    print(board)

    print(" --- " * 3)

    board = "|  " + game[2][0] + " |  " + game[2][1] + " |  " + game[2][2] + " |  "
    print(board)


turn = 1
print("Welcome to Tic Tac Toe Game!\nPlayer 1's mark is 'x' and Player 2's mark is 'o'\n\n")
while (True):
    if isDraw() == True:
        print("Game is drawn\n")
        exit()
    drawBoard()

    if turn == 1:
        print("Player 1's Turn:\n")
        x = int(input("Enter X:"))
        y = int(input("Enter y:"))
        x -= 1
        y -= 1
        game[x][y] = "x"
        turn = 2
        if whoWon() == True:
            print("Player 1 Win!")
            drawBoard()
            exit()
    else:
        print("Player 2's Turn\n")
        x = int(input("Enter X:"))
        y = int(input("Enter y:"))
        x -= 1
        y -= 1
        game[x][y] = "o"
        turn = 1
        if whoWon() == True:
            print("Player 2 Win!")
            drawBoard()
            exit()
