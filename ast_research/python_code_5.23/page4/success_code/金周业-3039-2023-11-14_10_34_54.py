list1=eval(input())
a=max(list1)
b=min(list1)
while list1.count(a)>0:
    list1.remove(a)
while list1.count(b)>0:
    list1.remove(b)
print(list1)

