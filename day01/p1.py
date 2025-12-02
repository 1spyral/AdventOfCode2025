# AOC 2025 Day 1 Problem 1

with open("input.txt", "r") as f:
    data = f.read()

num = 50
ans = 0

for line in data.split("\n"):
    if line[0] == "R":
        num += int(line[1:])
        num %= 100
    else:
        num -= int(line[1:])
        num %= 100

    if num == 0:
        ans += 1

print(ans)
