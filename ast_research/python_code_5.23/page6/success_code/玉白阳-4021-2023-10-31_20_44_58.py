from tkinter import N


n=eval(input())
n1=N
j1=2
j2=3
j3=1
j4=2
e=j1/1+j2/2
while n-2>0:
    e+=(j1+j2)/(j3+j4)
    j1,j2=j2,j2+j1
    j3,j4=j4,j3+j4
    n-=1
if n1==0:
    print(0)
elif n1==1:
    print("%.4f"%int(j1/1))
elif n1==2:
    print("%.4f"%j1/1+j2/2)
elif n1>=3:
    print("%.4f"%e)

