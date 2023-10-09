import numpy as np


def isSafe(currentBoard, rowNumber, columnNumber):
    for col in range(0, len(currentBoard)):
        if currentBoard[rowNumber][col] == 1:
            return False
    for row in range(0, rowNumber):
        if currentBoard[row][columnNumber] == 1:
            return False
    for row, col in zip(range(rowNumber, -1, -1), range(columnNumber, -1, -1)):
        if currentBoard[row][col] == 1:
            return False
    for row, col in zip(range(rowNumber, -1, -1), range(columnNumber, len(currentBoard))):
        if currentBoard[row][col] == 1:
            return False
    return True


def solveNQueen(currentBoard, numberOfQueens, rowNumber):
    if rowNumber >= numberOfQueens:
        return True

    for columnNumber in range(numberOfQueens):
        if isSafe(currentBoard, rowNumber, columnNumber):
            currentBoard[rowNumber][columnNumber] = 1
            if solveNQueen(currentBoard, numberOfQueens, rowNumber + 1):
                return True
            currentBoard[rowNumber][columnNumber] = 0

    return False


def NQueen_FindAllSolutions(allSolutions, currentBoard, numberOfQueens, rowNumber):
    if rowNumber == numberOfQueens:
        allSolutions.append(currentBoard.copy())
        return True

    for columnNumber in range(numberOfQueens):
        if isSafe(currentBoard, rowNumber, columnNumber):
            currentBoard[rowNumber][columnNumber] = 1
            NQueen_FindAllSolutions(allSolutions, currentBoard, numberOfQueens, rowNumber + 1)
            currentBoard[rowNumber][columnNumber] = 0

    return False


def printSolution(currentBoard):
    for row in range(len(currentBoard)):
        for col in range(len(currentBoard)):
            if currentBoard[row][col] == 1:
                print("Q", end=" ")
            else:
                print("_", end=" ")
        print()


# Driver Code

NumberOfQueens = 8
Board = np.zeros((NumberOfQueens, NumberOfQueens))
CopyBoard = Board.copy()


if solveNQueen(Board, NumberOfQueens, 0):
    print("First Solution:")
    printSolution(Board)
else:
    print("No Solution")

AllSolutions = []
NQueen_FindAllSolutions(AllSolutions, CopyBoard, NumberOfQueens, 0)
for i in range(len(AllSolutions)):
    print("Solution Number: ", i + 1)
    printSolution(AllSolutions[i])
    print()



