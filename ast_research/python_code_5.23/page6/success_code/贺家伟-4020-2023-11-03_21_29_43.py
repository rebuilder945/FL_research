h=eval(input())
N=eval(input())
H=0
for i in range(0,N-1):
    s=h
    h=h/2
    H=s+h
H=H+h
print(H)
