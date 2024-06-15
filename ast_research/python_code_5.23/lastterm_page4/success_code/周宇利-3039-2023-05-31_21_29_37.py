list1=eval(input())
a=max(list1)
b=min(list1)
for i in list1:
    while i==a:
        list1.remove(a)
    while i==b:
        list1.remove(b)
print(list1)
