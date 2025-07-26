import sys
input = sys.stdin.readline
total = 0
stack = []
K = int(input())
for _ in range(K):
    num = int(input())
    if num == 0:
        if stack:
            out = stack.pop()
            total -= out
    else:
        stack.append(num)
        total+=num
print(total)