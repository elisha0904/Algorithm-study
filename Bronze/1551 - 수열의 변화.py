n, k = list(map(int, input().split()))
a = list(map(int, input().split(',')))

def sequence(x):
    m = len(x)
    for i in range(m-1):
        x.append(x[i+1] - x[i])
    del x[0:m]
    return x

for _ in range(k):
    sequence(a)

a = list(map(str, a))
print(','.join(a))