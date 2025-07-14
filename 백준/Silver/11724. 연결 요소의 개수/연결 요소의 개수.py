import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def bfs(start):
    visited[start] = True
    q = deque()
    q.append(start)
    while q:
        node = q.popleft()
        for i in arr[node]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

count = 0
for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
        count+=1

print(count)