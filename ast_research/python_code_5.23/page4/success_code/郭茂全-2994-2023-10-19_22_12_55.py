list=input()
list1=[int(i) for i in list.split(",")]
n,m=eval(input())
a=len(list)
if -a-1<n<a:
    c=list[n]
    d=[c]*m
    list2=list1+d
    print(list2)
else:
    print('error')
