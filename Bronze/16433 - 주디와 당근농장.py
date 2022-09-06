n, r, c = list(map(int, input().split()))
x, y, F = [], [], []

# # 농장 만들기 --> 번갈아가며 v로 바꾸려고 했는데 실패
# for _ in range(n):
#     x.append('.')
#
# for _ in range(n):
#     F.append(x)

def farm(a, x, y):
    k = 0
    while k < n:
        a.append(x); k += 1
        if k == n:
            break
        a.append(y); k += 1
    return a


if (r+c)%2 == 0:
    farm(x, 'v', '.')
    farm(y, '.', 'v')
    farm(F, x, y)
else:
    farm(x, '.', 'v')
    farm(y, 'v', '.')
    farm(F, x, y)

for i in range(n):
    print(''.join(F[i]))