import numpy as np
import SudokuSolver


def stringToBoard(puzzle, boardSize):
    board = np.zeros((boardSize, boardSize))
    for i in range(0, len(puzzle)):
        if puzzle[i].isdigit():
            board[i // boardSize][i % boardSize] = int(puzzle[i])
    return board


# open sample file as string
with open('sudoku_samples.txt', 'r') as f:
    sudokuSamples = f.read()
    for samples in sudokuSamples.splitlines():

        initialBoard, numberOfSolutions, *solution = samples.split(':')
        boardSize = int(len(initialBoard) ** 0.5)
        Board = stringToBoard(initialBoard, boardSize)

        print("Solving:", initialBoard, " expecting ", numberOfSolutions, " solutions", end="...")

        if SudokuSolver.sudokuSolver(Board):
            print("Solution found!", end="...")
            if numberOfSolutions == '1':
                knownSolution = stringToBoard(solution[0], boardSize)
                if np.array_equal(Board, knownSolution):
                    print("Correct Solution")
                else:
                    print("Incorrect Solution")
            else:
                print(numberOfSolutions, " solutions were expected")





