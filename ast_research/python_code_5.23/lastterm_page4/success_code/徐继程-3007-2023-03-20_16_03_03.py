ls1=input()
n,m=eval(input())
if m>len(ls1) or n>len(ls1):
    print(error)
else:
    for i in range(n-m):
        del ls1[n]
    print(ls1)

