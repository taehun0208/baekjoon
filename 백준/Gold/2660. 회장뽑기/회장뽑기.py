import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = [[] for _ in range(N+1)]
scores = [0]*(N+1)
while True:
    a, b= map(int, input().strip().split())
    if (a<0) and (b<0):
        break
    else:
        arr[a].append(b)
        arr[b].append(a)

def bfs(start):
    visited = [-1]*(N+1)
    queue = deque()
    queue.append(start)
    visited[start] = 0
    while queue:
        node = queue.popleft()  
        for i in arr[node]:
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[node]+1
    return max(visited[1:])

min_score = float('inf')
for i in range(1, N+1):
    score = bfs(i)
    scores[i] = score
    min_score = min(min_score, score)

candidates = []
for i in range(1, N+1):
    if scores[i] == min_score:
        candidates.append(i)

print(min_score, len(candidates))
for i in candidates:
    print(i, end=" ")