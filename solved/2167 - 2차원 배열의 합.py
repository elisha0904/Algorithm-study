a, b = list(map(int, input().split()))
x = list(list(map(int, input().split())) for _ in range(a))
c = int(input())
y = list(list(map(int, input().split())) for _ in range(c))

def line(q, w, e, r):
    ans = 0
    for i in range(q-e):
        print(x[q+i][w:r])
        ans += sum(x[q+i][w:r])
    return print(ans)

for i in range(c):
    line(y[i][0], y[i][1], y[i][2], y[i][3])