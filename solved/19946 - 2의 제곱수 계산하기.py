x = int(input())
n = 64

# while x%2 == 0:
#     n = n-1
#     x = x//2
#
# print(n)

while True:
    if x%2 != 0:
        print(n)
        break
    else:
        n = n-1
        x = x//2

# x/2로 하면 틀리고 x//2로 하면 맞는 이유가 뭐지?