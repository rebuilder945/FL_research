h=eval(input())
N=eval(input())-1
eva=h
if N==1:
    print("%.2f"%eva)
else:
    while N>0:
        eva=eva+h
        h=h/2
        N=N-1
    print("%.2f"%eva)
