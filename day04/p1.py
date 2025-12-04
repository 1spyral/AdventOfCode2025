# AOC 2025 Day 4 Problem 1

with open("input.txt", "r") as f:
    data = f.read()

ans = 0

grid = data.split("\n")
m = len(grid)
n = len(grid[0])

def check(x, y):
    adj = 0
    for i, j in (
        (x - 1, y - 1),
        (x - 1, y),
        (x - 1, y + 1),
        (x, y - 1),
        (x, y + 1),
        (x + 1, y - 1),
        (x + 1, y),
        (x + 1, y + 1),
    ):
        if 0 <= i < n and 0 <= j < m and grid[j][i] == "@":
            adj += 1
    return adj < 4

ans = 0

for x in range(n):
    for y in range(m):
        if grid[y][x] == "@" and check(x, y): ans += 1

print(ans)
