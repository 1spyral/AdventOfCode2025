# AOC 2025 Day 5 Problem 1

with open("input.txt", "r") as f:
    data = f.read()

from bisect import insort, bisect_right

lower = []
upper = []

lines = data.split("\n")
index = 0

while lines[index] != "":
    lo, hi = map(int, lines[index].split("-"))
    insort(lower, lo)
    insort(upper, hi)
    index += 1

index += 1

ans = 0

while index < len(lines):
    check = bisect_right(lower, int(lines[index])) - 1
    if lower[check] <= int(lines[index]) <= upper[check]: ans += 1
    index += 1

print(ans)
