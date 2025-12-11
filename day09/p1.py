# AOC 2025 Day 9 Problem 1

with open("input.txt", "r") as f:
    data = f.read()

coords = [list(map(int, line.split(","))) for line in data.split("\n")]

n = len(coords)

ans = 0

for i in range(n):
    for j in range(i + 1, n):
        width = abs(coords[i][0] - coords[j][0]) + 1
        height = abs(coords[i][1] - coords[j][1]) + 1
        ans = max(ans, width * height)

print(ans)
