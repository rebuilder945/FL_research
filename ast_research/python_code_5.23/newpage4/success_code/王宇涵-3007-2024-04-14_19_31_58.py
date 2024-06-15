lst = eval(input())
n,m = eval(input())
if m<=n<=len(lst)-1:
    del lst[m:n]
    print(lst)
elif n<m<=len(lst)-1:
     del lst[n+1:m+1]
     print(lst)
else:
    print("error")
