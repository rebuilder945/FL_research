list1=eval(input())
list1=list(list1)
a=max(list1)
b=min(list1)
for x in list1:
    if x==a or x==b:
        list1.remove(x)
        print(list1)

