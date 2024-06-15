lst=eval(input())
n,m=eval(input())
if n<m and n<len(lst)and m<len(lst):
    del(lst[n:m])
    print(lst)
else:
    print("error")
