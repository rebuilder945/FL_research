list1=eval(input())
x=0
while 0 in list1:
    list1.remove(0)
    x+=1
list2=[0]
list3=list2*x
list4=list1+list3
print(list4)
