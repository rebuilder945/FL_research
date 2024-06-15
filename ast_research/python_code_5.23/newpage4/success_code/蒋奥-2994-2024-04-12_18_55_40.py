list1=list(map(int,input().split(',')))
n,m=map(int,input().split(','))
list2=[]
a=int(len(list1))
if n>=a:
    print("error")
else:
    list2.append(list1[n])
    list3=list2*m
    list4=list1+list3
    print(list4)

