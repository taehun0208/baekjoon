N = int(input())
rope = [int(input().rstrip()) for _ in range(N)]
rope.sort(reverse=True)
max = 0
for i in range(len(rope)):
    kg = rope[i] * (i+1)
    if max < kg:
        max = kg
print(max)
