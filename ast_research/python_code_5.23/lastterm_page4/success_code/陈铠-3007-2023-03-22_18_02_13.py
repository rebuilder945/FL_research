lst=eval(input())
n,m=eval(input())
if 0<=n<=len(lis)-1 :
    del lst[n:m]
    print(lst)
else:
    print("error")

