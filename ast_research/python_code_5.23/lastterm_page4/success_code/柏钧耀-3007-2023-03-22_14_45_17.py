lst=eval(input())
n,m=eval(input())
if n<m<9999999:
    del(lst[n:m])
    print(lst)
else:
    print("error")
