from tkinter import N


a =input().split(" ")
d= input().split(" ")
n = d[0]
m = d[1] 
a[n],a[m] = a[m],a[n]
print(a)

