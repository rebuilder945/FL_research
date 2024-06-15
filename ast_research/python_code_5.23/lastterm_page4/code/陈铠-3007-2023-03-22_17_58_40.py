lst=eval(input())
n,m=eval(input())
if 0<=n<=len(lis)-1 :
    del lis(n:m)
    print(lis)
else:
    print("error")

