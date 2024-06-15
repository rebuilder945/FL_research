a=eval(input())
n,m=eval(input())
if n<=len(a) and m<=len(a):
    f=n
    c=m-n
    for i in range(c):
        del a[f]
        f+=1
    print(a)

else:
    print("error")
