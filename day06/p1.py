# AOC 2025 Day 6 Problem 1

with open("input.txt", "r") as f:
    data = f.read()

rows = [list(filter(lambda x: x != "", line.split())) for line in data.split("\n")]

ans = 0

for i in range(len(rows[0])):
    operation = rows[-1][i]
    val = 0
    if operation == "*":
        val = 1
    for row in rows[0:-1]:
        if operation == "*":
            val *= int(row[i])
        else:
            val += int(row[i])
    ans += val

print(ans)
