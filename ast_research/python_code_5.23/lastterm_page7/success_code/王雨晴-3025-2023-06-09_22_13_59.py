dic = {}
list0 = input().split()
list1 = []
list2 = []
list3 = []
for i in range(len(list0)):
    dic[list0[i]] = list0.count(list0[i])
for i in dic:
    list1.append(dic[i])
max_number = max(list1)
for i in dic:
    if dic[i] == max_number:
        list2.append([i,dic[i]])
for i in range(len(list2)):
    list3.append(list2[i][0])
list3.sort()
for i in range(len(list3)):
    list3[i] = [list3[i],str(max_number)]
for i in range(len(list3)):
    answer = " ".join(list3[i])
    print(answer)

