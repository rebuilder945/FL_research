#高度反弹
h=eval(input())
N=eval(input())
s=h
while 0<=x<N:
    h=h-0.5 * h
    s+=2 * h
    print("%.2f"%s)

