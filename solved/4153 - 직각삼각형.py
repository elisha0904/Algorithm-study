# 0이라는 정수를 입력 받을 때까지 무한히 입력을 받는 게 이 문제의 포인트?
a = []
while True:
    #한 줄씩 입력을 받는다
    x = list(map(int, input().split()))
    #한 줄의 정수 리스트를 계산용 리스트에 추가
    a.append(x)
    #입력 받은 수 중에 0이 있으면 반복 종료
    if 0 in x:
        break

for i in range(len(a)-1):
    # 마지막 숫자가 반드시 빗변이 아닐 수도 있어서 조건을 일일이 부여해줌...
    # 조건문을 더 짧게 만들 수는 없을까?
    if a[i][0]**2 + a[i][1]**2 == a[i][2]**2 or a[i][1]**2 + a[i][2]**2 == a[i][0]**2 or a[i][0]**2 + a[i][2]**2 == a[i][1]**2 :
        print('right')
    else:
        print('wrong')