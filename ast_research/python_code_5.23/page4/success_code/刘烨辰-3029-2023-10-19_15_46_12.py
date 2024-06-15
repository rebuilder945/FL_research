list1 = input().split(",")
list2 = eval(input())
a = []
for i in range(0,len(list1)):
    a.append([list1[i],list2[i]])
print(a)
