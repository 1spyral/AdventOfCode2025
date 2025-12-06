# AOC 2025 Day 6 Problem 2

with open("input.txt", "r") as f:
    data = f.read()

ans = 0

lines = data.split("\n")

idx = 0
val = 0
op = ""

while idx < len(lines[0]):
    if lines[-1][idx] != " ":
        ans += val
        op = lines[-1][idx]
        if op == "*":
            val = 1
        else:
            val = 0
    num = 0
    for line in lines[:-1]:
        if line[idx] != " ":
            num *= 10
            num += int(line[idx])
    if num != 0:
        if op == "*":
            val *= num
        else:
            val += num
    idx += 1

ans += val

print(ans)
