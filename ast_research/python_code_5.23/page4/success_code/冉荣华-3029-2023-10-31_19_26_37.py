from tkinter import X


n = input().split(',')
n=list(n)
c = eval(input())
x=[]
for i in range(len(n)):
    m=[]
    m.append(n[i])
    m.append(c[i])
    x.append(m)
print(x)

