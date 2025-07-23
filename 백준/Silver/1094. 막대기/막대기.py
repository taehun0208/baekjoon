first_stick = 64
t = int(input())
sum = 0
cnt = 0
while first_stick != 0:
    if sum + first_stick <= t:
        sum+=first_stick
        cnt+=1
    first_stick//=2
    
    if t == sum:
        break
print(cnt)
