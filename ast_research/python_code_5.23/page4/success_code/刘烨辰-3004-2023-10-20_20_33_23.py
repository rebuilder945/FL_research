list1 = eval(input())
list2 = sorted(list1)
for x in list1:
    for i in range(2,int(x/2)+1):
        if not x%i and x > 2:
            list2.remove(x)
print(list2)
