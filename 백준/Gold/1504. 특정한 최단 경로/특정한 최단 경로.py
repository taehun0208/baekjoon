import sys
input = sys.stdin.readline
import heapq

N,E = map(int, input().split())
arr = [[] for i in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    arr[a].append((b,c))
    arr[b].append((a,c))

v1, v2 = map(int, input().split())

def dikstra(start):
    distance = [float('INF')] * (N+1)
    q = []
    heapq.heappush(q,(0, start))
    distance[start] = 0

    while q:
        curCost, curNode = heapq.heappop(q)
        if distance[curNode] < curCost:
            continue
        for i in arr[curNode]:
            cost = curCost + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

dist1 = dikstra(1)
dist_v1 = dikstra(v1)
dist_v2 = dikstra(v2)

path1 = dist1[v1] + dist_v1[v2] + dist_v2[N]
path2 = dist1[v2] + dist_v2[v1] + dist_v1[N]
answer = min(path1, path2)
print(answer if answer < float('inf') else -1)