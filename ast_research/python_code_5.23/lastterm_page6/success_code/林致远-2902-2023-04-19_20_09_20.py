from tkinter import Y


n = int(input())
sum = 0
a,b = 2,1
while n>0:
    sum = sum + a/b
    m = b
    b = a
    a = a+m
    n -= 1
print('%.4f' % sum)
