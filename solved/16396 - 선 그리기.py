n = int(input())
x = list(list(map(int, input().split())) for _ in range(n))
line = 0

# 정렬
for i in range(n):
    x[i].sort()
x.sort()

print(x)

# 겹치는 부분 찾아서 0으로 만들기
for i in range(n-1):
    if x[i][1] > x[i+1][0]:
        if x[i][1] <= x[i+1][1]:
            x[i][1], x[i+1][0] = 0, 0
        elif x[i][1] > x[i+1][1]:
            x[i+1][0], x[i+1][1] = 0, 0

# 1차원 리스트로 변경 후 0 제거
x = sum(x, [])
while 0 in x:
    x.remove(0)

# 길이 재기
for i in range(len(x)//2):
    line += x[(2*i)+1] - x[2*i]

print(x)
print(line)


