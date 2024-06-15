list=eval(input())
n,m=eval(input())
if n<=m:
    list2=list[:n]+list[m:]
    print(list2)
else:
    print('error')
