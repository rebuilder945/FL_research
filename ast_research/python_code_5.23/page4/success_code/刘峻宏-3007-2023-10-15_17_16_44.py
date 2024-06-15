a=eval(input())
n,m=eval(input())
if n<=len(a) and m<=len(a):
    i=n
    for i in range(m-n):
        del a[i]
        i+=1


else:
    print("error")
