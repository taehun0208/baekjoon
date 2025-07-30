start, end = map(int, input().split())
word_map = {
    1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six',
    7:'seven', 8:'eight', 9:'nine', 0:'zero'
    }
arr = []
for i in range(start, end+1):
    if i > 9:
        first = i//10
        second = i%10
        word = word_map[first] + word_map[second]
    else:
        word = word_map[i]
    arr.append((i,word))
arr.sort(key=lambda x: x[1])
cnt = 0
for idx, (num, _) in enumerate(arr):
    print(num,end=' ')
    if (idx+1)%10 == 0:
        print()