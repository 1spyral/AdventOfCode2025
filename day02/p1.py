# AOC 2025 Day 2 Problem 1

with open("input.txt", "r") as f:
    data = f.read()

from bisect import insort, bisect_right

low, high = [], []
highest = 0

for interval in data.split(","):
    lo, hi = map(int, interval.split("-"))

    insort(low, lo)
    insort(high, hi)
    highest = max(highest, hi)

str_highest = str(highest)

ans = 0

for i in range(1, int(str_highest[:len(str_highest) // 2]) + 1):
    num = int(str(i) + str(i))

    idx = bisect_right(low, num) - 1

    if idx >= 0 and low[idx] <= num <= high[idx]:
        ans += num

print(ans)
