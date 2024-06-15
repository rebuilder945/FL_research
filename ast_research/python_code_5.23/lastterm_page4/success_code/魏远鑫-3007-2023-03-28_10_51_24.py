lst=eval(input())
n,m=eval(input())
if n <= len(lst):
    del list[n:m]
else:
    print("error")
