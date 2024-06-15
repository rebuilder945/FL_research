def Convert(a):
    b=list(a.split(""))
a=input()
n,m=eval(input())
a[n],a[m]=a[m],a[n]
print(a)
