list1 = eval(input())
min_number = min(list1)
max_number = max(list1)
list2 = []
for i in range(len(list1)):
    if list1[i] != min_number and list1[i] != max_number:
        list2.append(list1[i]) 
print(list2)
