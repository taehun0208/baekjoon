import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
arr = [[] for _ in range(N+1)]
distance = [float('inf')]*(N+1)
for _ in range(M):
    a, b, c = map(int, input().strip().split())
    arr[a].append((b, c))

start, end = map(int, input().split())

def daikstra(start):
    # 먼저 시작 점에 해당하는 좌표를 입력하고 가중치를 0으로 설정
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 저장 된 값을 curCost와 curNode에 저장
        curCost, curNode = heapq.heappop(q)
        # 비교 후 진행할지 말지 선택
        if distance[curNode] < curCost:
            continue
        # 인접한 노드들 값 계산해서 비교하기
        for i in arr[curNode]:
            cost = curCost + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

daikstra(start)
# 최종적으로 가장 작은 cost를 가진 경로가 저장된다
print(distance[end])