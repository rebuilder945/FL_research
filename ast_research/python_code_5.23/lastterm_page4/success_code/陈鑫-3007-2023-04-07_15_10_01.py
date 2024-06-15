lst=eval(input())
n,m=eval(input())
if n-1>len(lst) or m-1>len(lst):
    print("error")
elif n<m:
    del lst[n,m]
elif n==m:
    del lst[n]
else:
    del lst[m,n]
print(lst)



