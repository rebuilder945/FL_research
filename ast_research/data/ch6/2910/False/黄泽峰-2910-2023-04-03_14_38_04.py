h = int(input())
N = int(input())
h1 = h
i = 1
if N == 1:
    s = h1
while N>1:
    s = h1+h
    h = h/2
    i = i+1
    if i == N:
        break
print("%.2f"%(s))

