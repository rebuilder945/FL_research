from re import A


h = eval(input())
N = eval(input())
a = h
for i in range(N-1):
    h = h*(1/2)
    a = a+2*h
print(a)
