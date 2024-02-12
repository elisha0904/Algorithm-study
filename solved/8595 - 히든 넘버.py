n = int(input())
x = list(map(str, input()))
result = 0


for i in range(n):
    if x[i].isalpha() == True:
        x[i] = ' '
    else:
        pass

a = ''.join(x).split()
a = list(map(int, a))


for i in range(len(a)):
    result += a[i]

print(result)



