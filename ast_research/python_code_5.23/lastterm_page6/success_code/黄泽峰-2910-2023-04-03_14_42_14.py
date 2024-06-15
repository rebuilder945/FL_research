h = int(input())
N = int(input())
h1 = h
i = 1
s = 0
while N>1:
    s = s+h1+h
    h = h/2
    i = i+1
    if i == N:
        break
if N ==1:
    s == h1
print("%.2f"%(s))

