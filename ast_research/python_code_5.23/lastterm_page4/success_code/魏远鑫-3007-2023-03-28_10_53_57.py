lst=eval(input())
n,m=eval(input())
if n<0 or m>len(list) or n>m:
    print("error")
else:
    del lst[n:m]
