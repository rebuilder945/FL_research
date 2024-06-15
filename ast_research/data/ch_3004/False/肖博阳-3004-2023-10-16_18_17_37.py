list1=eval(input())
list2=[]
for i in range(len(list1)):
    for a in range(2,i):
        if i % a ==1:
            list2.append(i)
print(list2)                  
