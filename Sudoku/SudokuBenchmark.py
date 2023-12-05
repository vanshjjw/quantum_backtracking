import copy
import random
import time
import numpy as np
import SudokuSolver
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

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


def benchmarkSpeedWithNumberOfClues():
    with open('sudoku_samples.txt', 'r') as f:
        samples = f.read().splitlines()

    results = open("Benchmark results/results.txt", "w")
    for i in range(0, 9):
        sample = samples[i]
        initialBoard, numberOfSolutions, *solution = sample.split(':')
        boardSize = int(len(initialBoard) ** 0.5)
        Board = stringToBoard(initialBoard, boardSize)

        print("Initial Board: ", initialBoard, end="\n\n")
        results.write("Initial Board: " + initialBoard + "\n\n")
        numberOfClues = np.count_nonzero(Board)
        plt.figure(i)

        Times = []
        clues = []
        while numberOfClues > 20:
            print("Number of Clues: ", numberOfClues, end="...")
            results.write("Number of Clues: " + str(numberOfClues) + "...")
            BenchmarkParams = {'numOfNodes': 0, "showEachStep": False, "ShowProgress": False}

            start = time.time()
            SudokuSolver.sudokuSolver(copy.deepcopy(Board), True, BenchmarkParams)
            end = time.time()
            Times.append(end - start)
            clues.append(numberOfClues)
            BenchmarkParams["Time"] = Times[-1]

            print("Number of Nodes: ", BenchmarkParams['numOfNodes'], " Time: ", BenchmarkParams["Time"],
                  end="\n\n")
            results.write("Number of Nodes: " + str(BenchmarkParams['numOfNodes']) + " Time: " + str(BenchmarkParams["Time"]) + "\n")

            removeRandomCLue(Board)
            numberOfClues = np.count_nonzero(Board)

        plt.plot(clues, Times, 'ro')
        plt.ylabel('Time')
        plt.xlabel('Number of Clues')
        plt.savefig('SpeedVsNumberOfClues ' + str(i) + '.png')

    results.close()

def removeRandomCLue(Board):
    nonZeroElementIndices = np.nonzero(Board)
    choice = np.random.randint(0, len(nonZeroElementIndices[0]))
    Board[nonZeroElementIndices[0][choice]][nonZeroElementIndices[1][choice]] = 0


# benchmarkSpeedWithNumberOfClues()
benchmarkSamples()