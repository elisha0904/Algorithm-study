x = list((input()))
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
k = []

for i in num:
    k.append(x.count(i))

a = divmod(k[6]+k[9], 2)
if a[1] != 0:
    k.append(a[0]+1)
else:
    k.append(a[0])

del k[6]; del k[8]
print(max(k))

