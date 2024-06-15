list1=eval(input())
for i in list1:
    while list1.count(i)!=1:
        
            list1.remove(i)
            continue
print(list1)
