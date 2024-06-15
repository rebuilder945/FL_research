ls1=input()
n,m=eval(input())
if m>len(ls1) or n>len(ls1):
    print(error)
else:
    del ls1[n,m]
    print(ls1)

