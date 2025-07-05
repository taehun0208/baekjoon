import sys
from collections import deque
input = sys.stdin.readline

N, M, start = map(int, input().split())
arr = [[] for _ in range(N+1)]
visited = [False]*(N+1)
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(1, N+1):
    arr[i].sort()

def dfs(node):
    print(node, end = " ")
    visited[node] = True
    for i in arr[node]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        node = queue.popleft()
        print(node, end = " ")
        for i in arr[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

dfs(start)
print()
visited = [False] * (N+1)
bfs(start)
