a=eval(input())
n,m=eval(input())
if n<-len(a) or n>=len(a) or m<-len(a) or m>=len(a):
    print("error")
else:
    b=[]
    b.append(a[n:m])
    a.remove(b)
    print(a)
