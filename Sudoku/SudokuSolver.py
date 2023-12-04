import time


def validBoard(board, num, pos):
    size = len(board)
    sizeOfBox = int(size ** 0.5)

    # check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    # check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // sizeOfBox  # Get x coordinate of box
    box_y = pos[0] // sizeOfBox  # Get y coordinate of box
    for i in range(box_y * sizeOfBox, box_y * sizeOfBox + sizeOfBox):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def heuristic(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j
    return None


# BenchmarkParams is a dictionary of parameters to be used for benchmarking
def sudokuSolver(board, benchmark=False, benchmarkParams=None):

    if benchmarkParams["ShowProgress"]:
        if time.time() - benchmarkParams["ShowProgress"] > 5:
            print(benchmarkParams['numOfNodes'], " nodes explored in 5 seconds")
            benchmarkParams["ShowProgress"] = time.time()

    findPosition = heuristic(board)
    if not findPosition:
        return True
    else:
        row, col = findPosition

    # Try numbers 1-9 serially (can be optimized)
    for i in range(1, 10):
        if benchmark:
            benchmarkParams['numOfNodes'] += 1
        if validBoard(board, i, (row, col)):
            board[row][col] = i
            if benchmarkParams["showEachStep"]:
                printBoardAsString(board, highlightCell=(row, col))
            if sudokuSolver(board, benchmark, benchmarkParams):
                return True
            board[row][col] = 0
    return False


def printBoard(board):
    sizeOfBox = int(len(board) ** 0.5)
    for i in range(len(board)):
        if i % sizeOfBox == 0 and i != 0:
            print("-----------------------")
        for j in range(len(board[0])):
            if j % sizeOfBox == 0 and j != 0:
                print("|", end=" ")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end=" ")


def printBoardAsString(board, highlightCell=None):
    sizeOfBox = int(len(board) ** 0.5)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if highlightCell and highlightCell == (i, j):
                print("\033[1;32;40m" + str(board[i][j]) + "\033[0m", end="")
            elif board[i][j] == 0:
                print(".", end="")
            else:
                print(board[i][j], end="")
        print("|", end=" ")
    print()
