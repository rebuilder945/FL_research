l=list()
n,m=map(int,eval(input()))
b=[]
if n>len(l)-1 or n<-len(l):
    print("error")
elif n<len(l)-1 or n>-len(l):
    a=l[n]
    b.append(a)
    c=b*m
print(l+c)
