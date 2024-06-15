lst=eval(input())
n,m=eval(input())
if n<0 or m>len(lst) or n>m:
    print("error")
else:
    del lst[n:m]
