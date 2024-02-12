x, y = list(int(input()) for _ in range(2))
result = []

num = list(i for i in range(x, y+1))

def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for i in num:
    if prime(i) == True:
        result.append(i)

if 1 in result:
    result.remove(1)

if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))