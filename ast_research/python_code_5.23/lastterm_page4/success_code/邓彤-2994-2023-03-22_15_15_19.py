a=list(eval(input()))
n,m=eval(input())
if n>=len(a) or n<-len(a):
    print("error")
else:
    b=a[n]
    i=0
    while i<m:
        a.append(b)
        i+=1
    print(a)
