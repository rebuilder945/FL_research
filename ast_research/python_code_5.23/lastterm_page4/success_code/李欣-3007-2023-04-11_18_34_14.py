ls1=list(input())
n,m=input().split(',')
n=int(n)
m=int(m)
if m<len(ls1) and n<len(ls1):
    if n>m:
        del ls1[m:n]
        print(ls1)
    elif n<m:
        del ls1[n:m]
        print(ls1)
    else:
        del ls1[n]
        print(ls1)
else:
    print("error")
