h = int(input())
N = int(input())
s = h
for i in range(1, N):
    s += h * pow(2 / 3, i) *2
s1 =pow(2 / 3, N) * h
print(round(s, 2)


