x = input().lower()
n = set(x) # 중복 제거
a = {}

for i in n:
    a[i] = x.count(i)
    # 개수 세서 딕셔너리에 집어넣기

b = list(a.values()) # 값 리스트
b.sort(reverse=True) # 값 리스트 내림차순 정렬

if len(b) == 1:
    print(max(a, key=a.get).upper()) # 길이가 1인 경우
elif b[0] == b[1]:
    print("?") # 최댓값이 2개 이상인 경우
else:
    print(max(a, key=a.get).upper())