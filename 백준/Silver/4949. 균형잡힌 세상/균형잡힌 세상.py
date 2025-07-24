import sys
input = sys.stdin.readline

while True:
    command = input().rstrip()
    if command == '.':
        break
    stack = []
    check = False
    for i in command:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] != '(':
                check = True
                break
            stack.pop()                
        elif i == ']':
            if not stack or stack[-1] != '[':
                check = True
                break
            stack.pop()

    if not check and not stack:
        print("yes")
    else:
        print("no")
