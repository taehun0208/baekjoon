import sys
input = sys.stdin.readline
import heapq
V, E = map(int, input().split())
K = int(input())

arr = [[] for _ in range(V+1)]
distance = [float('INF')] * (V+1)
for _ in range(E):
    u, v, w = map(int, input().strip().split())
    arr[u].append((v, w))
    
def dikstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        curCost, curNode = heapq.heappop(q)
        if distance[curNode] < curCost:
            continue
        for i in arr[curNode]:
            cost =  curCost + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dikstra(K)
for i in range(1, V+1):
    if distance[i] == float('inf'):
        print("INF")
    else:
        print(distance[i])
