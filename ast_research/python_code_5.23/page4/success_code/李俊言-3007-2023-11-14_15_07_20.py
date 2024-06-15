lis=eval(input())
n,m=eval(input())
a=len(lis)
if n>a-1 or m>a-1 or n>m:
    print("error")
else:
    for x in range(n,m):
        del lis[x]
        print(lis)





