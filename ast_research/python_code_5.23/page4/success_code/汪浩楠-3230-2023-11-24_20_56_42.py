from tkinter import N


lst=eval(input())
lst.sort()
n=1
a=0
for i in lst[::]:
    a+=i*n
    n*=10
print(a)
