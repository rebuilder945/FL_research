list=input()
n,m=eval(input())
if n<=m:
    del list[m:n]
    print(list)
else:
    print("error")
