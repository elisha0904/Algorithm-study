n = int(input())
x = list(list(int(input()) for _ in range(2)) for i in range(n))

def floor(a, b):
    f = []
    f.append(list(i+1 for i in range(b)))
    for i in range(a):
        f.append(list(sum(f[i][:j+1]) for j in range(b)))
    return print(f[a][b-1])

for i in range(len(x)):
    floor(x[i][0], x[i][1])