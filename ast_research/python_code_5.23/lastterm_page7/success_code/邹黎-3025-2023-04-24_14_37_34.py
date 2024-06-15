from tkinter import N


lst=list(input().split())
max=0
for x in lst:
    if lst.count(x)>=max:
        max=lst.count(x)
lst0=[]
for y in lst:
    if lst.count(y)==max:
        lst0.append(y)
for x in sorted(list(set(lst0))):
    print(x,max)
