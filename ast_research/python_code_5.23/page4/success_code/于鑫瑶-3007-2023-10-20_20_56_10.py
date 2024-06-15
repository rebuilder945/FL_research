ls1=input()
n,m=eval(input())
if n<len(ls1):
    if m<len(ls1) and n<m:
        del ls1[n:m]
        print(ls1)
    elif m<len(ls1) and n>m:
        del ls1[m:n]
        print(ls1)
    else:
        print("error")
else:
    print("error")
