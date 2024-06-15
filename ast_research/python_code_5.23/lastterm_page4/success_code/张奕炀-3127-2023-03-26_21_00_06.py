n = eval(input())
list1 = [i for i in range(n)]
list2 = list1.copy()
for i in range(len(list1)):
    if i < n-1:
        list1[i] = list2[i+1]
    else:
        list1[i] = list2[0]
print(list1)
