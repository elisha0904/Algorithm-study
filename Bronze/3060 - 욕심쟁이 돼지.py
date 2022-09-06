n = int(input())
x = list(list(input() for _ in range(2)) for i in range(n))

def pig(x, y):
    z = int(x)
    a = list(map(int, y.split()))
    b, k = sum(a), 1

    while True:
        # c = []

        # for i in range(6):
        #     if i <= 2:
        #         c.append(a[i] + a[i+3] + a[i-1] + a[i+1])
        #     elif i == 5:
        #         c.append(a[i] + a[i-3] + a[i-1] + a[i-5])
        #     else:
        #         c.append(a[i] + a[i-3] + a[i-1] + a[i+1])

        # a = c
        # b = sum(c)
        if b > z:
            break
        else:
            b = b * 4
            k += 1

    return print(k)

for i in range(len(x)):
    pig(x[i][0], x[i][1])