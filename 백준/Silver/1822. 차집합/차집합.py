import sys
input = sys.stdin.readline
a, b = map(int, input().split())
arr1 = set(map(int, input().split()))
arr2 = set(map(int, input().split()))
result = sorted(arr1-arr2)
print(len(result))
for re in result:
    print(re,end=" ")
