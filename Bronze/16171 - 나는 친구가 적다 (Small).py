x = list(input())
y = str(input())
n = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
k = []

# 숫자 제거하기 (isdigit() 메소드)
for i in x:
    if i.isdigit() == False:
        k.append(i)

X = ''.join(k)

if y in X:
    print(1)
else:
    print(0)