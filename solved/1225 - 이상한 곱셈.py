a, b = map(str, input().split())
a, b = list(map(int, a)), list((map(int, b)))

# 자릿수 각각 더해서 곱해주면 되는 것...
print(sum(a)*sum(b))

# k = 0
# for i in range(len(a)):
#     for j in range(len(b)):
#         k += int(a[i])*int(b[j])
#
# print(k) --> 시간 초과