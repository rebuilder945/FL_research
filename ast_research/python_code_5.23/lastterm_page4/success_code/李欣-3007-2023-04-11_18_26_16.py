ls1=list(input())
a=input()
n=a[0]
m=a[1]
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
