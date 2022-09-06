a, b = map(int,input().split())
x = [0]
k = 0

# 1은 1번, 2는 2번, 3은 3번...
for i in range(1,b+1):
  for j in range(i):
    x.append(i)

# 문제에서 주어진 구간 합산
for i in range(a, b+1):
    k += x[i]

print(k)