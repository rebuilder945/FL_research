list1=eval(input())
list2=[]
for i in list1:
    if i < 2:
        pass
    else:
        for x in range(2,):
            if x==0:
                pass
            elif i%x==0:
                list2.append(i)
            else:
                pass
print(list2)

