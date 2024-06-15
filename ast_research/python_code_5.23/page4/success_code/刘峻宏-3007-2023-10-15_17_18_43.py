a=eval(input())
n,m=eval(input())
if n<=len(a) and m<=len(a):
    i=n
    c=m-n
    for i in range(c):
        del a[i]
        i+=1


else:
    print("error")
