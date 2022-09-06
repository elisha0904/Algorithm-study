n = int(input())
m = list(input() for _ in range(n))
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def pgrm(z):
    x, y = 0, 0
    k = []

    # 공백 제거
    z = list(z.replace(' ', '').lower())

    for i in range(len(z)):
        if z[i].isalpha() == True:
            k.append(z[i])

    while len(k) > 0 :
        for i in range(len(a)):
            if a[i] in k:
                k.remove(a[i])
                x += 1
        if x == len(a):
            x = 0
            y += 1

    if y == 1:
        return 'Pangram!'
    elif y == 2:
        return 'Double pangram!!'
    elif y >= 3:
        return 'Triple pangram!!!'
    else:
        return 'Not a pangram'


for i in range(n):
    print('Case {}:'.format(i+1), pgrm(m[i]))