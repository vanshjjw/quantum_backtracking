import time
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
    samples = f.read().splitlines()

    # First 9 samples are easy
    for i in range(18, 20):
        initialBoard, numberOfSolutions, *solution = samples[i].split(':')
        boardSize = int(len(initialBoard) ** 0.5)
        Board = stringToBoard(initialBoard, boardSize)
        NumberOfClues = np.count_nonzero(Board)

        print("Benchmarking:", initialBoard, " expecting ", numberOfSolutions, " solutions",
              " given clues ", NumberOfClues, end="\n")

        BenchmarkParams = {'numOfNodes': 0, "Time": 0, "showEachStep": False, "ShowProgress": time.time()}
        start = time.time()
        SudokuSolver.sudokuSolver(Board, True, BenchmarkParams)
        end = time.time()
        BenchmarkParams["Time"] = end - start

        print("Number of Nodes: ", BenchmarkParams['numOfNodes'], " Time: ", BenchmarkParams["Time"], end="\n\n")



