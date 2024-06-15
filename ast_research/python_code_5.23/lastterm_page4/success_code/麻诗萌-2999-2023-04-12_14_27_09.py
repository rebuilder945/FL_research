from tkinter import Y


lst=input().split()
n,m=map(int,input().split())
lst[n],lst[m]=x,y
lst[m],lst[n]=x,y
print(lst)
