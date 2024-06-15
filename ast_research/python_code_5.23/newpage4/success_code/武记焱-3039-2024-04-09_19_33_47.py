list1=eval(input())
x=max(list1)
y=min(list1)
while x in list1:
    list1.remove(x)
while y in list1:
     list1.remove(y)
print(list1)
