a=list(eval(input()))
n,m=eval(input())
b=a[n]
if n>=len(a) or n<-len(a):
    print("error")
else:
    i=0
    while i<m:
        a.append(b)
        i+=1
    print(a)
