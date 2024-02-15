'''
N보다 작거나 같은 자연수 중에서, 집합 K의 원소로만 구성된 가장 큰 수를 출력하는 프로그램을 작성하시오.
K의 모든 원소는 1부터 9까지의 자연수로만 구성된다.

예를 들어 N=657이고, K={1, 5, 7}일 때 답은 577이다.

[입력]

첫째 줄에 N, K의 원소의 개수가 공백을 기준으로 구분되어 자연수로 주어진다. (10 ≤ N ≤ 100,000,000, 1 ≤ K의 원소의 개수 ≤ 3)
둘째 줄에 K의 원소들이 공백을 기준으로 구분되어 주어진다.
각 원소는 1부터 9까지의 자연수다.

단, 항상 K의 원소로만 구성된 N보다 작거나 같은 자연수를 만들 수 있는 경우만 입력으로 주어진다.

[출력]

첫째 줄에 N보다 작거나 같은 자연수 중에서, K의 원소로만 구성된 가장 큰 수를 출력한다.

'''

from itertools import product

N, _ = list(map(int, input().split()))
K = list(map(str, input().split()))
lenN = len(str(N))

while True:
    cases = list(product(K, repeat=lenN))
    candidates = []

    for c in cases:
        now = int(''.join(c))
        if now <= N:
            candidates.append(now)
    
    if len(candidates) >= 1:
        print(max(candidates))
        break
    else:
        lenN -= 1


'''
메모리 32140 KB
시간      44 ms
코드 길이 410 B
'''