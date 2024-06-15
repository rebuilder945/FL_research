l=list(eval(input()))
n,m=eval(input())
if n>len(l)-1 or n<-len(l):
    print("error")
else:
    while m>0:
        l.append(l[n])
        m-=1
    print(l)
