import sys

# input()으로 여러 줄 입력 받으며 value error 발생하는 것으로 추정
# 떄문에 sys.stdin.readline() 함수를 통해 여러 줄을 입력 받음
b = [sys.stdin.readline().strip().split() for i in range(4)]
a = sum(b, [])

x1 = int(a[0])+int(a[1])
x2 = x1-int(a[2])+int(a[3])
x3 = x2-int(a[4])+int(a[5])
x4 = x3-int(a[6])+int(a[7])

# 리스트로 만들어 max()로 최댓값 구하기
x = (x1,x2,x3,x4)
print(max(x))
