list1=eval(input())
list3=list1
while 0 in list1:
    list1.remove(0)
    list2=list1
m=len(list3)
n=len(list2)
while m>n:
    list2.append(0)
    print(list2,end="")

