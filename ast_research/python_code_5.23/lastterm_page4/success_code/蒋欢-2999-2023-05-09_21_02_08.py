def Change(ls,n,m):
    ls[n],ls[m]=ls[m],ls[n]
    print(ls)
ls=input()
n,m=eval(input())
ls=ls.split(" ")
Change(ls,n,m)
