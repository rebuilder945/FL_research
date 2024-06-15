lst = eval(input())
n,m = eval(input())
if n<=m<=len(lst)-1:
    del lst[n:m]
    print(lst)
elif m<n<=len(lst)-1:
    del lst[m:n]
    print(lst)
else:
    print("error")
