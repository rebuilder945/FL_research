list=[eval(input())]
n,m=eval(input())
a=len(list)
if -a-1<n<a:
    c=list[n]
    d=[c]*m
    list2=list+d
    print(list2)
else:
    print('error')
