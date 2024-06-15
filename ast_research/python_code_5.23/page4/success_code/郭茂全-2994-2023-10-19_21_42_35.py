list=[eval(input())]
n,m=eval(input())
a=len(list)
b=-a
if b<=n<=-1 or 0<=n<=a-1:
    c=list[n]
    d=list.pop(n)
    e=[c]*m
    list1=d+e
    print(list1)
else:
    print('error')
