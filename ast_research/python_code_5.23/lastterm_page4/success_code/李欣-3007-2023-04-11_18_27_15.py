ls1=list(input())
a=input()
n=int(a[0])
m=int(a[1])
if m>=len(ls1) and n>=len(ls1):
    if n>m:
        del ls1[m,n]
        print(ls1)
    elif n<m:
        del ls1[n,m]
    else:
        del ls1[n]
else:
    print("error")
