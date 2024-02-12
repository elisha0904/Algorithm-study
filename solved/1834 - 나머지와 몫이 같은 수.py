x = int(input())
n = 1
ans = []

while x > n:
    ans.append(x * n + n)
    n += 1

print(sum(ans))