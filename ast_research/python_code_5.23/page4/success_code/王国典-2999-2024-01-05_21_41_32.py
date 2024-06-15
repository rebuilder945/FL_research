ls=input().split(" ")
ls2=input().split(" ")
x=ls[eval(ls2[0])]
y=ls[eval(ls2[1])]
ls[eval(ls2[0])]=y
ls[eval(ls2[1])]=x
print(ls)
