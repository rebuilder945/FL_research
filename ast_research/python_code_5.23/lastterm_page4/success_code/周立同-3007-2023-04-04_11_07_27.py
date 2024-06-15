lst=eval(input())
n,m=eval(input())
if n<m and 0<=n<len(lst) and 0<=m<len(lst):
    del lst[n:m]
    print(lst)
else:
    print("error")
