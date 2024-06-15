from re import L
from tkinter import N
f=0
g=0

m=input()
c=[]
for i in range(len(m)):
    c.append(int(m[i]))
for t in range(len(c)):
    c[t]=(c[t]+5)%10


f=c[0]
c[0]=c[-1]
c[-1]=f
if len(m)>=4:
  g=c[1]
  c[1]=c[-2]
  c[-2]=g
for s in range  (len(c)): 
    print(c[s],end='')   
