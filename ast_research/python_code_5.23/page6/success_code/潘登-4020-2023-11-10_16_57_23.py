h=eval(input())
N=eval(input())
H=h
if N == 1:
    print("{:.2f}".format(h))
else:
    for i in (1,N):
        s=H+2*h*0.5**i
    print("{:.2f}".format(s))    
