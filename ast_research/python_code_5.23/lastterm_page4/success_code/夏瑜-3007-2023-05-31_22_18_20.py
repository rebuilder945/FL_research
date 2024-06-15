lst=eval(input())
n,m=eval(input())
if n>0 and n<=len(lst) and m>0 and m<=len(lst) and n<=m:
    print(lst[:n]+lst[m:])
else:
    print(error)

