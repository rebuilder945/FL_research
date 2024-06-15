lis=eval(input())
n,m=eval(input())
a=len(lis)
if n>a-1 or m>a-1 or n>m or n<m<=0:
    print("error")
else:
    for x in range(n,m):
        b=n
        del lis[b]
    print(lis)






