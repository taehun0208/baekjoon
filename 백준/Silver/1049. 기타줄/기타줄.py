N, M = map(int, input().split())
min_pack = float('inf')
min_piece = float('inf')
for _ in range(M):
    a, b = map(int, input().split())
    min_pack = min(min_pack, a)
    min_piece = min(min_piece, b)

cost1 = N*min_piece
cost2 = (N//6) * min_pack + (N%6)*min_piece
cost3 = ((N+5)//6) * min_pack
print(min(cost1, cost2, cost3))