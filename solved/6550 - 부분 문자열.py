'''
2개의 문자열 s와 t가 주어졌을 때 s가 t의 부분 문자열인지 판단하는 프로그램을 작성하라. 
부분 문자열을 가지고 있는지 판단하는 방법은 t에서 몇 개의 문자를 제거하고 이를 순서를 바꾸지 않고 합쳤을 경우 s가 되는 경우를 이야기 한다.

[입력]
입력은 여러 개의 테스트 케이스로 이루어져 있다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 문자열 s 와 t가 빈칸을 사이에 두고 들어온다. s와 t의 길이는 10만을 넘지 않는다.

[출력]
입력된 s와 t의 순서대로 s가 t의 부분 문자열인 경우 Yes라 출력하고 아닐 경우 No라고 출력한다.
'''

# 입력 여러 줄 어떻게 받는지 잊어버려서 한참 헤맸네

import sys

# while문 내부에 try 안 넣었더니 틀림 (입력 종료를 고려해야 함!)
while True:
    try:
        line = sys.stdin.readline()
        S, T = line.strip().split()

        S = list(S)

        for t in T:
            try:
                if S[0] == t:
                    S.pop(0)
                    continue
            except:
                break

        if len(S) == 0:
            print('Yes')
        else:
            print('No')
    except:
        break

'''
메모리 31120 KB
시간      48 ms
코드 길이 407 B
'''