# AOC 2025 Day 11 Problem 2

with open("input.txt", "r") as f:
    data = f.read()

from collections import defaultdict

lines = data.split("\n")

graph = defaultdict(list)

for line in lines:
    segments = line.split()
    device = segments[0][:-1]
    for out in segments[1:]:
        graph[device].append(out)

memo = {
    "out": (1, 0, 0)
} # (general, first, both)

def dp(node = "svr"):
    if node in memo:
        return memo[node]
    general = 0
    first = 0
    both = 0
    for i in graph[node]:
        g, f, b = dp(i)
        general += g
        first += f
        both += b
    if node in ["fft", "dac"]:
        both += first
        first += general
    memo[node] = (general, first, both)
    return memo[node]

general, first, both = dp()

print(both)
