l=[eval(input())]
n,m=eval(input())
b=[]
if n<0:
    if n<-len(l):
        print("error")
    if n>=-len(l):
        a=l[n]
        b.append(a)
        c=b*m
        print(l+c)
if n>=0:
    if n<=len(l)-1:
        a=l[n]
        b.append(a)
        c=b*m
        print(l+c)
    if n>len(l)-1:
        print("error")
