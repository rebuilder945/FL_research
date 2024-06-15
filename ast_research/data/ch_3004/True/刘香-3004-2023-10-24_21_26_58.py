list1=eval(input())
list2=[]
for i in list1:
    if i>=2:
        for x in range(2,i):
            if(i%x)==0:
                break
        else:
            list2.append(i)

print(list2)
    
