lst=eval(input())
n,m=eval(input())
if  0<n<=m<=len(lst):
    print(lst[:n]+lst[m:])
else:
    print(error)

