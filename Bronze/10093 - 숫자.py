a, b = map(int, input().split())

if a>b:
    A = a; B = b; C = A-B-1
elif a<b:
    A = b; B = a; C = A-B-1
else:
    C = 0

print(C)

for i in range(C):
    print(B+i, end=' ')