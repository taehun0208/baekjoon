import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline

V, E, R = map(int, input().split())
arr = [[] for _ in range(V+1)]
visited = [0] * (V+1)
cnt = 1
for _ in range(E):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(R):
    global cnt
    visited[R] = cnt
    arr[R].sort()
    for i in arr[R]:
        if visited[i] == 0:
            cnt+=1
            dfs(i)

dfs(R)
for i in range(1, V+1):
    print(visited[i])