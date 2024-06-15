list1=eval(input())
a=max(list1)
b=min(list1)
for i in list1:
    if i == a or i == b:
        list1.remove(i)
print(list1)

