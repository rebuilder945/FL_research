list1=eval(input())
list2=[]
for x in list1:
    for y in range(2,x):
        if x%y!=0:
            list2.append(x)
print(list2)
