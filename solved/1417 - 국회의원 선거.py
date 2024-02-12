n = int(input())
p = [int(input()) for i in range(n)]
a, k = 0, p[0]
p.pop(0)

if n == 1 or k > max(p):
    a = 0
else:
    while k <= max(p):
        p[p.index(max(p))] = int(p[p.index(max(p))])-1
        k += 1
        a += 1

        if k == max(p):
            a += 1
            break

print(a)

# while p[0] != max(p):
#     print(p)
#     print(p.index(max(p)))
#
#     if n == 1 or p[0] > max(p):
#         a = 0
#         break
#
#     if p[0] == max(p):
#         a += 1
#
#     p[p.index(max(p))] = int(p[p.index(max(p))])-1
#     p[0] = int(p[0])+1
#     a += 1




