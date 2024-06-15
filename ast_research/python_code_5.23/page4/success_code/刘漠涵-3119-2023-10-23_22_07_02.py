list1=eval(input())
list2=[]
for i in list1[-1:-8:-1]:
    if bool(i in list2)==False:
        list2.append(i)
list2.reverse()
print(list2)
