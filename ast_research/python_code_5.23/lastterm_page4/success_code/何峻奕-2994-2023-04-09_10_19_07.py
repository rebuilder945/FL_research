l=[eval(input())]
n,m=eval(input())
b=[]
if n>len(l)-1 or n<-len(l):
    print("error")
if n<len(l)-1 or n>-len(l):
    a=l[n]
    b.append(a)
    c=b*m
    print(l+c)
