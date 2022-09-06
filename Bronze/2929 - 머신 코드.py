x = list(input())
a = []
k = 0

for i in range(len(x)):
    if x[i].isupper():
        a.append(i)

for i in range(len(a)-1):
    k += 4-(a[i+1]-a[i])

print(k)