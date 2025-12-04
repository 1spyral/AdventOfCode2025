# AOC 2025 Day 3 Problem 1

with open("input.txt", "r") as f:
    data = f.read()

ans = 0

for line in data.split("\n"):
    highest = 0
    second_highest = 0
    for i in range(len(line) - 1):
        if int(line[i]) > highest:
            highest = int(line[i])
            second_highest = 0
        elif int(line[i]) > second_highest:
            second_highest = int(line[i])
    second_highest = max(second_highest, int(line[-1]))

    ans += highest * 10 + second_highest

print(ans)
