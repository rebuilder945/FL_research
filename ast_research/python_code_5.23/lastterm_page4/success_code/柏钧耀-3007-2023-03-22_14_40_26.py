lst=eval(input())
n,m=eval(input())
if n<m or n<len(lst)or m<len(lst):
    del(lst[n:m])
    print(lst)
else:
    print("error")
