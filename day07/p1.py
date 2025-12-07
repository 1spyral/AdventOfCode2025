# AOC 2025 Day 7 Problem 1

with open("input.txt", "r") as f:
    data = f.read()

grid = [list(row) for row in data.split("\n")]

ans = 0

for i, row in enumerate(grid[:-1]):
    for j, val in enumerate(row):
        if val in ["S", "|"]:
            if grid[i + 1][j] == "^":
                ans += 1
                grid[i + 1][j - 1] = "|"
                grid[i + 1][j + 1] = "|"
            else:
                grid[i + 1][j] = "|"

print(ans)
