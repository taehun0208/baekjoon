import sys
input = sys.stdin.readline

N = int(input())
E = int(input())

arr = [[] for _ in range(N+1)]
visited = [False] * (N+1)
cnt = -1

for i in range(E):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(start):
    visited[start] = True
    global cnt
    cnt+=1
    for i in arr[start]:
        if visited[i] == 0:
            dfs(i)

dfs(1)
print(cnt)