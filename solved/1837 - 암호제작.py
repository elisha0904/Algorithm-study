## 답은 나오지만 시간 초과로 실패.
## 시간 단축할 수 있는 방법을 찾아봐야 할 것 같음.

a, b = map(int, input().split())
c = 2
x = []

# 소인수분해
while c <= a:
    if a % c == 0:
        x.append(c)
        a = a/c
    else:
        c = c+1

if x[0] < x[1] < b:
    print('BAD', x[0])
elif x[1] <= x[0] < b:
    print('BAD', x[1])
else:
    print('GOOD')