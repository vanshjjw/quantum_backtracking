import time
import numpy as np
import SudokuSolver

def stringToBoard(puzzle, boardSize):
    board = np.zeros((boardSize, boardSize))
    for i in range(0, len(puzzle)):
        if puzzle[i].isdigit():
            board[i // boardSize][i % boardSize] = int(puzzle[i])
    return board


def benchmarkSamples():
    with open('sudoku_samples.txt', 'r') as f:
        samples = f.read().splitlines()

        for i in range(0, 10):
            initialBoard, numberOfSolutions, *solution = samples[i].split(':')
            boardSize = int(len(initialBoard) ** 0.5)
            Board = stringToBoard(initialBoard, boardSize)
            numberOfClues = np.count_nonzero(Board)

            print("Benchmarking:",initialBoard," with ",numberOfClues," clues, "," expecting ",numberOfSolutions, " solutions.")

            BenchmarkParams = {'numOfNodes': 0, "Time": 0, "showEachStep": False, "ShowProgress": time.time()}
            start = time.time()
            SudokuSolver.sudokuSolver(Board, True, BenchmarkParams)
            end = time.time()
            BenchmarkParams["Time"] = end - start

            print("Number of Nodes: ", BenchmarkParams['numOfNodes'], " Time: ", BenchmarkParams["Time"], end="\n\n")

