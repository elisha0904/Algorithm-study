n = int(input())
# 2차원 리스트로 입력 받음
x = [list(map(int, input().split())) for _ in range(n)]
Q1 = []; Q2 = []; Q3 = []; Q4 = []; AXIS = []

for i in range(n):
    if x[i][0] == 0 or x[i][1] == 0:
        AXIS.append(x[i])
    elif x[i][0] > 0:
        if x[i][1] > 0:
            Q1.append(x[i])
        elif x[i][1] < 0:
            Q4.append(x[i])
    else:
        if x[i][1] < 0:
            Q3.append(x[i])
        elif x[i][1] > 0:
            Q2.append(x[i])

print("Q1: {}".format(len(Q1)))
print("Q2: {}".format(len(Q2)))
print("Q3: {}".format(len(Q3)))
print("Q4: {}".format(len(Q4)))
print("AXIS: {}".format(len(AXIS)))
