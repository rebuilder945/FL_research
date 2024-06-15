ls1=list(input())
nm=eval(input())
n=nm[0]
m=nm[1]
if n not in ls1 or m not in ls1:
    print("error")
else:
    ls1.remove(range(n,m))
    print(ls1)
