list1 = input().split(',')
list2 = input().split(',')
l = len(list1)

list = []
for i in range (l):
    list.append([list1[i], int(list2[i])])

list.sort(key=lambda x:x[1],reverse=False)
print(list)

