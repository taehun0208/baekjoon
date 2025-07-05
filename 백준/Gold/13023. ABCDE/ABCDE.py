import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [ [] for _ in range(n)]

for _ in range(m):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(start, visited, cnt):
    global goal
    if cnt == 4:
        goal = 1
        return
    
    visited[start] = True
    for i in arr[start]:
        if not visited[i]:
            dfs(i, visited, cnt+1)
    visited[start] = False

for i in range(n):
    goal = 0
    visited = [False for _ in range(n)]
    dfs(i, visited, 0)
    if goal == 1:
        break

if goal:
    print(1)
else:
    print(0)