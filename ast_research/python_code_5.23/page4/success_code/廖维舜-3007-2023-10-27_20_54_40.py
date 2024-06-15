list=input()
n,m=eval(input())
if 0<=n<=m<=len(list)-1:
    print(list[0:n]+list[m:])
else:
    print(error)
