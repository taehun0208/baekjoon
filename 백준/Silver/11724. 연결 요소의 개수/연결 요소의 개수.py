import sys
input = sys.stdin.readline
sys.setrecursionlimit(2000)

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(start):
    visited[start] = True
    for i in arr[start]:
        if not visited[i]:
            dfs(i)
count = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        count+=1

print(count)