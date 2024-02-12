# 입력 받는 게 까다로운 문제였음 (단어 개수만 알려주고 줄바꿈이 얼마나 있는지를...)
x = []

while True:
    try:
        x.append(list(map(str, input().split())))
    except EOFError:
        break

x = sum(x, []) # n차원 리스트 1차원으로

todo = ['Re', 'Pt', 'Cc', 'Ea', 'Tb', 'Cm', 'Ex']
t = [0, 0, 0, 0, 0, 0, 0]

for i in range(len(x)):
    for j in todo:
        if x[i] == j:
            t[todo.index(j)] += 1

p = [0, 0, 0, 0, 0, 0, 0]

for i in range(len(p)):
    p[i] = t[i] / len(x)

for i in range(7):
    print('{} {} {:.2f}'.format(todo[i], t[i], p[i]))

print('Total {} 1.00'.format(len(x)))
