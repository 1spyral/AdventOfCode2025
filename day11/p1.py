# AOC 2025 Day 11 Problem 1

with open("input.txt", "r") as f:
    data = f.read()

from collections import defaultdict

lines = data.split("\n")

ans = 0

graph = defaultdict(list)

for line in lines:
    segments = line.split()
    device = segments[0][:-1]
    for out in segments[1:]:
        graph[device].append(out)

def traverse(node = "you"):
    if node == "out":
        global ans
        ans += 1
        return
    for i in graph[node]:
        traverse(i)

traverse()

print(ans)
