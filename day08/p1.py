# AOC 2025 Day 8 Problem 1

with open("input.txt", "r") as f:
    data = f.read()

CONNECTIONS = 1000

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

graph = [[] for _ in range(n)]

for _ in range(CONNECTIONS):
    _, i, j = heapq.heappop(edges)
    graph[i].append(j)
    graph[j].append(i)

visited = [False for _ in range(n)]

def traverse(n):
    size = 1
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            size += traverse(i)
    return size

ans = [0, 0, 0]

for i in range(n):
    if not visited[i]:
        heapq.heappushpop(ans, traverse(i))

print(ans[0] * ans[1] * ans[2])
