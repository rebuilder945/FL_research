ls1=eval(input())
n,m=eval(input())
if n<=len(ls1) and m<=len(ls1):
    for i in range(n,m):
        del ls1[i]
    print(ls1)
else:
    print("error")
