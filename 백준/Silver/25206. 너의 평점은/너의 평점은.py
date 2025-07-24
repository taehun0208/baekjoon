# 입력 값을 분할하여 총 학점과 과목별 평점 값을 계산하여 출력하는 형태이며 과목별 평점은 딕셔너리로 구현

rating = {
    "A+" : 4.5,
    "A0" : 4.0,
    "B+" : 3.5,
    "B0" : 3.0,
    "C+" : 2.5,
    "C0" : 2.0,
    "D+" : 1.5,
    "D0" : 1.0,
    "F" : 0
}

total = 0 # 총 학점
result = 0 # 학점 * 과목별 평점

for _ in range(20):
    c, s, p = input().split()
    s = float(s)
    if p != 'P':
        total += s
        result += s * rating[p]
print("%.6f" % (result/total))
