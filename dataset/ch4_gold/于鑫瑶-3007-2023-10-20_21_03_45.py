ls1=eval(input())
n,m=eval(input())
if n<len(ls1):
    if m<len(ls1) and n<m:
        del ls1[n:m]
        print(ls1)
    else:
        del ls1[m+1:n+1]
        print(ls1)
else:
    print("error")
