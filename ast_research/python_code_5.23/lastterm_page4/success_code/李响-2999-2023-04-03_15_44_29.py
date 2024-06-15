from tkinter import N


a =input().split(" ")
d= input().split(" ")
n = a[0]
m = a[1] 
a[n],a[m] = a[m],a[n]
print(a)

