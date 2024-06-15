list1=eval(input())
list2=[]
for i in list1:
    for a in range(2,i):
        if i % a ==0:
            list2.append(i)
for x in list1:
    if x in list2:
        list1.remove(x)
list(set(list1))        
print(list1)       
                
