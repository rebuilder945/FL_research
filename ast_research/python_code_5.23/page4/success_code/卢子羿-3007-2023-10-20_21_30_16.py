lst=eval(input())
n,m=eval(input())
if n<=m and n<max(lst):
    del lst[n:m]
    print(lst)
else:
    print("error")

