list1=eval(input())
list2=[]
for x in list1:
    if x>=2:
        for y in range(2,x,1):
            if x%y==0:
                break
        else:
            list2.append(x)
print(list2)
