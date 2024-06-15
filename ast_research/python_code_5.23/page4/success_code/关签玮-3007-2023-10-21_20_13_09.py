lst=eval(input())
n,m=eval(input())
if m<len(lst):
    del lst[n:m]
    print(lst)
else:print("error")
