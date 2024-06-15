list1=eval(input())
m=max(list1)
a=min(list1)
list2=[]
for i in list1:
    for n in list(range(a,m)):
       if i%n!=0:
            list2.append(i)
        
print(list2)
