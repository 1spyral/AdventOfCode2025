# AOC 2025 Day 8 Problem 2

with open("input.txt", "r") as f:
    data = f.read()

from math import sqrt
import heapq

boxes = [list(map(int, line.split(","))) for line in data.split("\n")]

n = len(boxes)

edges = []

def distance(i, j):
    return sqrt((boxes[i][0] - boxes[j][0]) ** 2 + (boxes[i][1] - boxes[j][1]) ** 2 + (boxes[i][2] - boxes[j][2]) ** 2)

for i in range(n):
    for j in range(i + 1, n):
        heapq.heappush(edges, (distance(i, j), i, j))

parents = [i for i in range(n)]
wired = set([0])

def find(n):
    if parents[n] == n:
        return n
    leader = find(parents[n])
    parents[n] = leader
    if leader == 0:
        wired.add(n)
    return leader

def union(i, j):
    leader_i, leader_j = find(i), find(j)
    parents[leader_i] = min(leader_i, leader_j)
    parents[leader_j] = min(leader_i, leader_j)

prev_i, prev_j = 0, 0

while len(wired) < n:
    _, i, j = heapq.heappop(edges)
    union(i, j)
    prev_i, prev_j = i, j
    for x in range(n): find(x)

print(boxes[prev_i][0] * boxes[prev_j][0])
