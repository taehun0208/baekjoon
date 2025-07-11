import sys
from collections import deque
input = sys.stdin.readline

V, E, R = map(int, input().split())
arr = [[] for _ in range(V+1)]
visited = [0] * (V+1)
cnt = 1
for _ in range(E):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
for i in range(1, V+1):
    arr[i].sort()

def bfs(start):
    global cnt
    queue = deque()
    queue.append(start)
    visited[start] = cnt
    while queue:
        node = queue.popleft()  
        for i in arr[node]:
            if visited[i] == 0:
                cnt+=1
                visited[i] = cnt
                queue.append(i)
bfs(R)

for i in range(1, V+1):
    print(visited[i])