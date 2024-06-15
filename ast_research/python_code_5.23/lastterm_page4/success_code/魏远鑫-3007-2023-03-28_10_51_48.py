lst=eval(input())
n,m=eval(input())
if n <= len(lst):
    del lst[n:m]
else:
    print("error")
