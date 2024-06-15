lst=eval(input())
n,m=eval(input())
if n-1>len(lst) or m-1>len(lst):
    print("error")
elif n<m:
    lst.pop(n,m)
elif n==m:
    lst.pop(n)
else:
    lst.pop(m,n)
print(lst)
