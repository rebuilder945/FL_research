lst = eval(input())
n,m = eval(input())
if n<=m and m+1<=len(lst):
    del lst[n:m]
    print(lst)
else:
    print("error")
