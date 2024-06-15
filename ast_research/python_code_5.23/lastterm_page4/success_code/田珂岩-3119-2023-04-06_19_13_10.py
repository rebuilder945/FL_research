list1 = eval(input())
for i in range(int(len(list1))):
    while list1.count(i) > 1:
        list1.remove(i)
print(list1)        

