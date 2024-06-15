from tkinter import E


a=input()
b=eval(input())
c=[]
for i in a :
    if i==",":
       continue
    else:
        c.append(i)
d=[]
for x in range(len(b)):
    e=[[c[x],b[x]]]
    d=d+e
print(d)            


