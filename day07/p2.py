# AOC 2025 Day 7 Problem 2

with open("input.txt", "r") as f:
    data = f.read()

grid = [list(row) for row in data.split("\n")]

ans = 0

def visit(x, y, val):
    if grid[x][y] == ".":
        grid[x][y] = 1 if val == "S" else val
    else:
        grid[x][y] += 1 if val == "S" else val

for i, row in enumerate(grid[:-1]):
    for j, val in enumerate(row):
        if val == "S" or type(val) == int:
            if grid[i + 1][j] == "^":
                visit(i + 1, j - 1, val)
                visit(i + 1, j + 1, val)
            else:
                visit(i + 1, j, val)

print(sum(map(lambda x: x if x != "." else 0, grid[-1])))
