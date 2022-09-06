a, b, c = list(map(int, input().split()))

# 판매대수 : n
# 총 비용 = 고정비용 + 가변비용 = a + b*n
# 순 수익 = c*n - (a+b*n) > 0 이 될 때가 손익분기점

# n = 1
# B, C = 0, 0
#
# if b >= c:
#     print(-1)
# else:
#     while C-(a+B)<0:
#         B = B+b
#         C = C+c
#         n = n+1
#         print(B, C, n)
#         if C-(a+B)>=0:
#             print(n)
#             break


if b>=c:
    print(-1)
else:
    cost = c-b
    print(int(a/cost)+1)