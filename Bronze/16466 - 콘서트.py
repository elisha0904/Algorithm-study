x = int(input())
y = list(map(int, input().split()))

T = list(sorted(y))

for i in range(1, T[-1]+1):
    if i != T[i-1]:
        print(i)
        exit(0)

print(x+1)
