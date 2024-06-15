h=input(eval())
N=input(int())
if N==1:
    print("%.2f"%h)
else:
    while N>0:
        h+=h*0.5
        N-=1
    print("%.2f"%h)
