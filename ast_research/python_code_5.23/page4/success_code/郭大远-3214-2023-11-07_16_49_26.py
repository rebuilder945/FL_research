list1=eval(input())
for x1 in list1:
    if x1==0:
        list1.remove(x1)
        list1.append(0)
print(list1)
