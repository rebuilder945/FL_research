list=[eval(input())]
n,m=eval(input())
a=len(list)
b=-a
if b<=n<=-1 or 0<=n<=a-1:
    c=list[n]
    d=[c]*m
    list1=list+d
    print(list1)
else:
    print('error')
