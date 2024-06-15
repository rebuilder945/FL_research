ls1=input()
n,m=input()
n=int()
m=int()
if n<len(ls1):
    if m<len(ls1) and n<m:
        del ls1[n:m]
        print(ls1)
    elif m<len(ls1) and n>m:
        del ls1[m+1:n+1]
        print(ls1)
else:
    print("error")
