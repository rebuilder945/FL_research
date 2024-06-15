h = int(input())
N = int(input())
i = 1
s = h
while N>1:
    s = s+h
    h = h/2 
    i = i+1
    if i == N:
        break
if N == 1:
    s = s
print("%.2f"%(s))

