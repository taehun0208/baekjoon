import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
tree = [[] for _ in range(N+1)]
parent = [0] * (N+1)
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def BFS(start):
    q = deque()
    q.append(start)
    visited = [False] * (N+1)
    visited[start] = True
    while q:
        next = q.popleft()
        for i in tree[next]:
            if not visited[i]:
                visited[i] = True
                parent[i] = next
                q.append(i)

BFS(1)

for i in range(2, N+1):
    print(parent[i])