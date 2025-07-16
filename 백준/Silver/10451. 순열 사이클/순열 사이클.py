import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
result = []
for _ in range(T):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [False] * (N+1)
    cnt = 0

    def bfs(start):
        q = deque()
        q.append(start)
        visited[start] = True
        while q:
            now = q.popleft()
            next = arr[now]
            if not visited[next]:
                visited[next] = True
                q.append(next)

    for i in range(1, N+1):
        if visited[i] == 0:
            bfs(i)
            cnt+=1

    result.append(cnt)
for res in result:
    print(res)    