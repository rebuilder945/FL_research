list1=eval(input())
for i in list1:
    while True:
        list1.remove(i)
        if list1.count(i)==1:
            break
print(list1)
