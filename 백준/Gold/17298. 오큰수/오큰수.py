import sys
N=int(input())
answer=[-1 for i in range(N)]
a=list(map(int,sys.stdin.readline().split()))
check=[]

check.append(0)
for i in range(1,N):
    while check and a[check[-1]]<a[i]:
        answer[check.pop()]=a[i]
    check.append(i)
print(*answer)
