from tkinter import Y


lst=input().split()
n,m=map(int,input().split())
lst1=lst.copy()
x,y=lst[n],lst[m]
lst1[m]=x
lst1[n]=y
print(lst1)
