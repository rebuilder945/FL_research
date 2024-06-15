lis=eval(input())
n,m=eval(input())
length=len(lis)
if n<=m and n<length and m<=length:
    for i in range(n,m,1):
        del lis[i]
    print(lis)
else:
    print("error")
