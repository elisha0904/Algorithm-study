a = list(map(int, input().split()))
b = list(map(int, input().split()))
A, B, C, D = 0, 0, 0, 0

for i in range(10):
    if a[i] > b[i]:
        A += 1
        C = "A"
    elif a[i] < b[i]:
        B += 1
        C = "B"
    elif a[i] == b[i]:
        D += 1

# for i in range(10):
#     if a[i] > b[i]:
#         A += 1
#     elif a[i] < b[i]:
#         B += 1
#     elif a[i] == b[i]:
#         D += 1
#         if a[i-1] > b[i-1]:
#             C = "A"
#         elif a[i-1] < b[i-1]:
#             C = "B"
#         else:
#             pass
        # 이 코드가 간과한 점 : 계속 무승부가 나다가 마지막에 한 쪽이 이길 경우?


s_a, s_b = A*3+D*1, B*3+D*1
if s_a > s_b:
    print(s_a, s_b)
    print("A")
elif s_a < s_b:
    print(s_a, s_b)
    print("B")
elif s_a == s_b:
    print(s_a, s_b)
    if s_a == 10 and s_b == 10:
        print("D")
    else:
        print(C)
