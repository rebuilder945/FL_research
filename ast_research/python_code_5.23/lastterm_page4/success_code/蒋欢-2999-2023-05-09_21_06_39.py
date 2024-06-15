def Change(ls,n,m):
    ls[n],ls[m]=ls[m],ls[n]
    print(ls)
ls=input()
a=input()
ls=ls.split(" ")
a=a.split(" ")
n,m=int(a[0]),int(a[1])
Change(ls,n,m)
