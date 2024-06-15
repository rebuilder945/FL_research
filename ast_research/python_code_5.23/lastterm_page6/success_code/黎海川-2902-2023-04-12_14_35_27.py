from tkinter import Y


a=2
b=1
n=eval(input())
ts=0
while n>0:
    ts+=a/b
    c=b
    b=a
    a+=c
    n-=1
print("%.4f"%ts)


