n = int(input())
a = list(map(int, input().split()))
b, c = list(map(int, input().split()))
result = []

for i in range(n):
    k = divmod(a[i]-b, c)
    # a[i] (학생 수)가 총 감독관이 감독하는 사람의 수보다 적은 경우도 생각해야 함
    # 이 경우에는 나눗셈이 진행되지 않기 때문
    if a[i] < b:
        result.append(1)
    else:
        if k[1] != 0:
            result.append(k[0]+2)
        elif k[1] == 0:
            result.append(k[0]+1)

print(int(sum(result)))
