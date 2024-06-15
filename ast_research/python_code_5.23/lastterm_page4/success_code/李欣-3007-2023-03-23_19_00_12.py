ls1=list(eval(input()))
n,m=eval(input())
if n in ls1:
    if m not in ls1:
        print("error")
    else:
        ls2=ls1.remove(range(n,m))
        print(ls2)
else:
    print("error")
