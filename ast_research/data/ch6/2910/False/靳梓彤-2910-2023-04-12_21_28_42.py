h=int(input())
N=int(input())
for i in range(N):
    if i:
        i=1
        h=h
    else:
        h=h+h/2
print(h)
