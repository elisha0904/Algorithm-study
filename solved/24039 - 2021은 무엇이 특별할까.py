# n = int(input())
# x = [2, 3]
#
# # 소수 찾기 알고리즘
#
# # if n == 1:
# #     print('6')
# #     exit(0)
#
# for i in range(2, n):
#     prime = True
#     for j in range(2, i):
#         if i == 2:
#             break
#         if i > j and i % j == 0:
#             prime = False
#             break
#         else:
#             continue
#     if prime:
#         x.append(i)
#
#     if len(x) > 2:
#         if x[-1] * x[-2] > n:
#             break
#
# print(x[-1] * x[-2])

x = []
while True:
    x.append(input())
    if x[-1] == '':
        break