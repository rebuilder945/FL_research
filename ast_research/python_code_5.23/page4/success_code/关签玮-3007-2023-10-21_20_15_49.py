lst=eval(input())
n,m=eval(input())
if n<m<len(lst)or n<m==len(lst):
    del lst[n:m]
    print(lst)
else:print("error")
