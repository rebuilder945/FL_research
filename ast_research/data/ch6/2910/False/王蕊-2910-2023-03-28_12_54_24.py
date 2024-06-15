#高度反弹
h=eval(input())
N=eval(input())
s=h
i=0
while 0<=i<N:
    i=i+1
    h=h-0.5 * h
    s+=2 * h
    print("%.2f"%s)

