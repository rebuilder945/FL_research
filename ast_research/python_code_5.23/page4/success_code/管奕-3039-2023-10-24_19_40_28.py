from ast import Del


list=eval(input())
a=max(list)
b=min(list)
list1=list.copy()
for x in list:
    if x==a or x==b:
        list.remove(x)
print(list1)
