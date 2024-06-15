a=input().split(",")
a=[int(i) for i in a]
b=len(a)
n,m=eval(input())
if n>b-1 or n<-b:
    print ("error")
else:
    c=a[n]
    for i in range(m):
        a.append(c)
        print(a)
