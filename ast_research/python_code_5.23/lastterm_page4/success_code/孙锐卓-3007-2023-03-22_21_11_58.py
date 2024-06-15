lst=input()
n,m=input().split(",")
n, m = int(n), int(m)
lst=eval(lst)
if n >= len(lst) or m >= len(lst):
    print("error")
else:
    del lst[n:m]
    print(lst)

