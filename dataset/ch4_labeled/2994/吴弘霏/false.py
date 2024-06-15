a=list(eval(input()))
n,m=eval(input())
b=[]
if n>len(a) or n<-len(a):
    print("error")
else:
    for i in range(m):
        b.append(a[n])
        c=a+b
        print(c)

