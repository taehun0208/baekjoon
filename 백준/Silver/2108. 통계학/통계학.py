import sys
from collections import Counter
input = sys.stdin.readline
N = int(input())
num_list = [int(input()) for _ in range(N)] 
print(round(sum(num_list) / N))
num_list.sort()
print(num_list[N//2])
counter = Counter(num_list)
mode_freq = counter.most_common()
max_freq = mode_freq[0][1]
modes = [num for num, freq in mode_freq if freq == max_freq]
modes.sort()
print(modes[1] if len(modes) > 1 else modes[0])
print(max(num_list)-min(num_list))
