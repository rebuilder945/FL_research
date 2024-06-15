lst=eval(input())
n,m=eval(input())
if 0<n<=m and m<=len(lst):
    del lst[n:m]
    print(lst)
elif n>len(lst) or m>len(lst):
    print("error")
