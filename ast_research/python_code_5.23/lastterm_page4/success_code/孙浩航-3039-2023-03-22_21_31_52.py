list1=eval(input())
a=max(list1)
b=min(list1)
while a  in list1:
    list1.remove(a)
list2=list1
while b in list2:
    list2.remove(b) 
print(list2)  
