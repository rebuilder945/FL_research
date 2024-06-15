lst=eval(input())
n,m=eval(input())
if n>len(lst) or m>len(lst):
    print("error")
else:
    lst.remove(lst[n+1,m])
    print(lst)
