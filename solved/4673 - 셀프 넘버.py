num = list(i for i in range(1, 10000))
inhere = []

def d(x):
    k = list(str(x))
    numx = 0
    for i in range(len(k)):
        numx += int(k[i])
    return x + numx

for i in num:
    inhere.append(d(i))

for i in num:
    if i in inhere:
        continue
    print(i)

