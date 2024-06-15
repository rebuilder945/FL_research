lst=eval(input())
n,m=eval(input())
if  0<=n<=m<=len(lst):
    del lst[n:m]
    print(lst)
else:
    print("error")

