ls1=list(eval(input()))
nm=eval(input())
n=nm[0]
m=nm[1]
if n in ls1:
    if m not in ls1:
        print("error")
    else:
        ls2=ls1.remove(range(n,m))
        print(ls2)
else:
    print("error")
