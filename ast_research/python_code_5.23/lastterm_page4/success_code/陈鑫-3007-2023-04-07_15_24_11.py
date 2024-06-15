lst=eval(input())
n,m=eval(input())
if n-1>len(lst) or m-1>len(lst):
    print("error")
elif n<m:
    for i in range(n,m):
        lst.pop(i)
    print(lst)
elif n==m:
    pass
else:
    for i in range(m,n):
        lst.pop(i)
    print(lst)
