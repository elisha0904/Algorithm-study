# # 첫 번째 코드
#
# a, b, v = list(map(int, input().split()))
# d = 0
#
# while v > 0:
#     v -= a
#     if v <= 0:
#         d += 1
#         break
#     v += b
#     d += 1
#
# print(d)


a, b, v = list(map(int, input().split()))

# divmod는 (몫, 나머지)의 tuple로 출력
x = divmod(v - b, a - b)
# v를 a - b로 나누면 '마지막 날 전날에 어디까지 갔는지' 알 수 있음
# 즉, 나머지 값이 0보다 작으면 이튿날 오전에 끝. 그러나 나머지가 0이면 당일에 끝.

if x[1] == 0 :
    print(x[0])
else:
    print(x[0] + 1)