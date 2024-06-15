h = int(input())
N = int(input())
H = h
while N>1:
    N = N-1
    a = h/2
    H = H + 2*a
    if N ==0:
        break
print "%.2f"%H
