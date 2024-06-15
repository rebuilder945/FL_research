lst=eval(input())
n,m=eval(input())
if n<=m and n>=0 and m<=len(lst) :
    del lst[n:m]
    print(lst)
else:
    print("error")


