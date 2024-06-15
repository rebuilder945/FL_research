from re import M
from tkinter import Y


a=2
b=1
c=int(input())
s=0
while c>0:
    s+=a/b
    d=b
    b=a
    a+=d
    c-=1
print('%.4f'%s)
