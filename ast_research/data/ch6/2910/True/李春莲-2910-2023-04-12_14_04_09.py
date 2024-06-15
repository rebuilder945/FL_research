h=eval(input())
N=eval(input())-1
eva=h
if N==1:
    print("%.2f"%h)
else:
    while N>0:
        eva+=h*0.5*2
        h*=0.5
        N-=1
    print("%.2f"%eva)
