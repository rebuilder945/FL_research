lst=eval(input())
n,m=eval(input())
if n-1>len(lst) or m-1>len(lst):
    print("error")
elif n<m:
    del lst[n,m]
    print(lst)
elif n==m:
    del lst[n]
    print(lst)
else:
    del lst[m,n]
    print(lst)



