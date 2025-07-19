import sys
sys.setrecursionlimit(10**6)

def appendstr(LEN):
    if LEN == 1:
        return['*']

    stars = appendstr(LEN//3)
    L = []

    for S in stars:
        L.append(S*3)
    for S in stars:
        L.append(S+' '*(LEN//3)+S)
    for S in stars:
        L.append(S*3)
    return L
n = int(sys.stdin.readline().strip())
print('\n'.join(appendstr(n)))