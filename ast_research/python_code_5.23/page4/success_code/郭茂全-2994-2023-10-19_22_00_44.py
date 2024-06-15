list=input()
list1=list.split(",")
n,m=eval(input())
a=len(list)
if -a-1<n<a:
    c=list[n]
    d=[c]*m
    list2=list1+d
    b=','.join(map(str,list2))
    print(b)
else:
    print('error')
