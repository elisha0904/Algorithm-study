n = int(input())
x = list(input() for _ in range(n))

# '단, 같은 단어가 여러 번 입력된 경우에는 한 번 씩만 출력한다.'
k = list(set(x))

k.sort()
k.sort(key = len)

for i in range(len(k)):
    print(k[i])