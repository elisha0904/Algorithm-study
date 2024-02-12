x = list(map(int, input().split()))
a = min(x)

while True:
    n = 0

    for i in x:
        if a % i == 0:
            n += 1
    if n == 3:
        break

    a += 1

print(a)