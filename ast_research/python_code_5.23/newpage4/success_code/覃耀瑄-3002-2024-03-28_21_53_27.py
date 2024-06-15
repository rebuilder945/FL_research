list1=eval(input())
m=max(list1)
a=min(list1)
for i in list1:
    for n in range(2,i):
       if i%n==0:
           list1.remove(i)
 
        
print(list1)
