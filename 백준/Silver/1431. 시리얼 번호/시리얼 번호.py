import sys
input = sys.stdin.readline
N = int(input())
arr = [input().rstrip() for _ in range(N)]

def sumdigit(s):
    return sum(int(c) for c in s if c.isdigit())

sorted_arr = sorted(arr, key=lambda x: (len(x), sumdigit(x),x))
for so in sorted_arr:
    print(so)