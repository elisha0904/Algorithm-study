import string
import random
string = string.ascii_lowercase

n = int(input())
x = list(map(str, input()))

pt = [i for i in range(len(x)) if '?' in x[i]]

for k in pt:
    x[k] = x[n-k-1]
    if x[n-k-1] == '?':
        x[n-k-1] = random.choice(string)
        x[k] = x[n-k-1]

result = "".join(x)
print(result)