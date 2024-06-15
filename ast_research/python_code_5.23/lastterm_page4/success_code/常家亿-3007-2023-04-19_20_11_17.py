lst =eval(input())
n,m = eval(input())
a = len(lst)
if n < -a or n >= a or m < -a or m >= a:
    print("error")
else:
    del lst[n:m]
    print(lst)
