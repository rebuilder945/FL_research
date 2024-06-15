lst=eval(input())
n,m=eval(input())
if n<m<=len(lst):
    del lst[n,m]
else:
    print("error")
