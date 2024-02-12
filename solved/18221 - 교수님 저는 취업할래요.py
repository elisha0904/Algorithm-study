n = int(input())
room = list(list(map(int, input().split())) for _ in range(n))

# 교수와 성규의 좌표값 찾기
pf, st = [], []

for i in range(n):
    for j in range(n):
        if room[i][j] == 5:
            pf.append(i)
            pf.append(j)
        elif room[i][j] == 2:
            st.append(i)
            st.append(j)


# 교수와 성규 사이 거리가 5 이상이어야 하는 조건 (미충족시 0 출력 후 종료)
x = ((pf[0] - st[0]) ** 2 + (pf[1] - st[1]) ** 2) ** (1/2)

if x >= 5:
    pass
else:
    print('0')
    exit(0)

# 교수랑 성규 사이에 다른 학생이 3명 이상 있는지 확인
p = 0
y, z = min([pf[0], st[0]]), min([pf[1], st[1]])

for i in range(abs(pf[0]-st[0])+1):
    for j in range(abs(pf[1]-st[1])+1):
        if room[y + i][z + j] == 1:
            # print(y+i, z+j)
            p += 1

# print(p)

if p >= 3:
    print('1')
else:
    print('0')
