n = eval(input())
list1 = [i for i in range(1,n+1)]
list2 = []
for x in range(1,n+1):
    list2.append(list1[x])
list2.append(list1[0])
print(list2)



