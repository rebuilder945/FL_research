list=[eval(input())]
n,m=eval(input())
a=len(list)
if -a<=n<=a-1:
    c=list[n]
    d=[c]*m
    list1=list+d
    print(list1)
else:
    print('error')
