lst =[1,2,3,4,5,6]
n,m = 7,3
a = len(lst)
if n < -a or n >= a or m < a or m >= a:
    print("error")
else:
    del lst[n:m]
    print(lst)
