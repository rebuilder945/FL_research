ls=input().split(" ")
a,b=eval(input())
x=ls[a]
y=ls[b]
ls[a]=y
ls[b]=x
print(ls)
