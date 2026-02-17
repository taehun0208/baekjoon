def solution(slice, n):
    answer = 1
    while(n - answer*slice) >0:
        answer = answer+1
    return answer