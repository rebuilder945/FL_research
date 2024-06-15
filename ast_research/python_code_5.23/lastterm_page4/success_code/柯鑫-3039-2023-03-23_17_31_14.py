list1=input()
a=max(list1)
b=min(list1)
for x in list1:
    if x==a:
        list1.remove(a)
        print(list1)
    elif x==b:
        list1.remove(b)
        print(list1)

