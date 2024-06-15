h = eval(input())
N = eval(input())
s = h
for i in range(1,N):
    h = h/2
    s += 2*h
print("%.2f"%s)
