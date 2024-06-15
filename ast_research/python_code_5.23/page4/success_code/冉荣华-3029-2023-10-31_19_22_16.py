from tkinter import X


n = input().split(',')
n=list(n)
c = eval(input())
zipped=zip(n,c)
x=[]
x.append(zipped)
print(list(x))
