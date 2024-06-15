list1=eval(input())
list2=list1.copy()
for i in list2:
    if i < 2:
        list2.remove(i)
for x in range(2,int(i**0.5)+1):
    if i%x==0:
       list2.remove(i)
print(list2)        

