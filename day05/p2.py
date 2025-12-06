# AOC 2025 Day 5 Problem 2

with open("input.txt", "r") as f:
    data = f.read()

from bisect import insort

lower = []
upper = []

lines = data.split("\n")
index = 0

while lines[index] != "":
    lo, hi = map(int, lines[index].split("-"))
    insort(lower, lo)
    insort(upper, hi)
    index += 1

ans = 0

index = 0

for i in range(len(lower)):
    lo, hi = lower[i], upper[i]
    if index < lo:
        index = lo
        ans += 1
    ans += max(0, hi - index)
    index = max(hi, index)

print(ans)
