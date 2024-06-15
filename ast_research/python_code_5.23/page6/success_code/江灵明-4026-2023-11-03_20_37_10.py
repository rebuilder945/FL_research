from tkinter import Y


n = int(input())
x = 2
y = 1
a =0
while n>0:
    a = a+x/y
    m = y
    y = x
    x = x +m
    n-=1
print("%.4f"%a)
    
