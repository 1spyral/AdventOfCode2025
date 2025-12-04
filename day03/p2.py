# AOC 2025 Day 3 Problem 2

with open("input.txt", "r") as f:
    data = f.read()

ans = 0

for line in data.split("\n"):
    highest = [0 for _ in range(12)]
    
    n = len(line)
    for index, val in enumerate(line):
        digit = int(val)
        for i in range(max(12 - n + index, 0), 12):
            if digit > highest[i]:
                highest[i] = digit
                for j in range(i + 1, 12):
                    highest[j] = 0
                break

    joltage = 0

    for i in highest:
        joltage *= 10
        joltage += i
    
    ans += joltage

print(ans)
