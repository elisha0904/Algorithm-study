k = list(map(int, str(input())))
x = list(reversed(k))

for i in range(len(x)):
    if x[i] >= 5:
        try:
            x[i+1] += 1
        except:
            continue
        x[i] = 0
    else:
        if i != len(x)-1:
            x[i] = 0

x.reverse()
x = list(map(str, x))
print(''.join(x))