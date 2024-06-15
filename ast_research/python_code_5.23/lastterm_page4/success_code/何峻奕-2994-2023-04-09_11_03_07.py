l=list(map(int,input().split(",")))
n,m=eval(input())
b=[]
if (n<-len(l) or n>len(l)-1):
        print("error")
else:
    a=l[n]
    b.append(a)
    c=b*m
    print(l+c)

