t = int(input())
stack = []
num = list(map(int, input().split()))
check = 1

for i in num:
    if i == check:
        check += 1
    else:
        while stack and stack[-1] == check:
            stack.pop()
            check += 1
        stack.append(i)

while stack and stack[-1] == check:
    stack.pop()
    check += 1

if not stack:
    print("Nice")
else:
    print("Sad")
