n, x = int(input()), list(map(int, input().split()))

x.sort(reverse=True)
M = x[0]

for i in range(n):
    x[i] = x[i]/M * 100

print(sum(x)/n)