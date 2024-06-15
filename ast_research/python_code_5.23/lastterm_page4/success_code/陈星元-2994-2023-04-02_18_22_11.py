list=input().split(',')
Newlist=[]
for x in list:
    Newlist.append(int(x))
n,m=eval(input())
if n in range(-len(list),len(list)):
    x=Newlist[n]
    list2=[x]*m
    list3=Newlist+list2
    print(list3)
else:
    print("error")



