n = int(input())
y = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    x = []
    a, b, c = y[i]
    # for문으로 호실 리스트 생성
    for j in range(a):
        for m in range(b):
            x.append([j+1, m+1])
    # 2차원 리스트의 두 번째 값을 기준으로 오름차순 정렬
    x.sort(key=lambda x: x[1])
    result = x[c-1][0]*100 + x[c-1][1]
    print(result)