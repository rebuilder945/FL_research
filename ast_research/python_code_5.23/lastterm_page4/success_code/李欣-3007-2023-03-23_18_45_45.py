ls1=list(input())
nm=eval(input())
n=nm[0]
m=nm[1]
if n in ls1 and m in ls1:
    ls2=ls1.remove(range(n,m))
    print(ls2)
else:
    print("error")
