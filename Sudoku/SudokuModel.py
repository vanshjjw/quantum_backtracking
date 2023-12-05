import numpy as np
import pyomo.environ as pyo

N = 9

model = pyo.ConcreteModel()
model.I = pyo.RangeSet(0, N)
model.J = pyo.RangeSet(0, N)
model.K = pyo.RangeSet(0, N)

model.x = pyo.Var(model.I, model.J, model.K, within=pyo.Binary)

# Each cell must have exactly one number
model.unique_cells = pyo.ConstraintList()
for i in model.I:
    for j in model.J:
        model.unique_cells.add(sum(model.x[i, j, k] for k in model.K) == 1)

# Each number must appear exactly once in each row
model.rows = pyo.ConstraintList()
for i in model.I:
    for k in model.K:
        model.rows.add(sum(model.x[i, j, k] for j in model.J) == 1)

# Each number must appear exactly once in each column
model.columns = pyo.ConstraintList()
for j in model.J:
    for k in model.K:
        model.columns.add(sum(model.x[i, j, k] for i in model.I) == 1)

# Each number must appear exactly once in each 3x3 box
box_size = int(N ** 0.5)
model.boxes = pyo.ConstraintList()
for i in range(0, N, box_size):
    for j in range(0, N, box_size):
        for k in model.K:
            model.boxes.add(
                sum(model.x[i + di, j + dj, k] for di in range(box_size) for dj in range(box_size)) == 1
            )


# Test Board
sample = "000000000302540000050301070000000004409006005023054790000000050700810000080060009"
board = np.array([int(c) for c in sample]).reshape((N, N))

# Add known values
model.known = pyo.ConstraintList()
for i in model.I:
    for j in model.J:
        if board[i - 1][j - 1] != 0:
            model.known.add(model.x[i, j, board[i - 1][j - 1]] == 1)

# Solve
solver_exec_path = 'C:\\glpk\\w64\\glpsol'
solver = pyo.SolverFactory('glpk', executable=solver_exec_path)
solution = solver.solve(model)
print(solution)



