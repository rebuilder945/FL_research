list1=eval(input())
list2=[]
for x in list1:
    for x1 in range(2,x):
        if  x%x1==0:
            list1.remove(x)
list2=list1
print(list2)

        



