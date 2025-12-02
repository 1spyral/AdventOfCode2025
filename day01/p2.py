# AOC 2025 Day 1 Problem 2

with open("input.txt", "r") as f:
    data = f.read()

num = 50
ans = 0

for line in data.split("\n"):
    for i in range(int(line[1:])):
        if line[0] == "R":
            num += 1
        else:
            num -= 1
        num %= 100
        if num == 0:
            ans += 1

print(ans)
