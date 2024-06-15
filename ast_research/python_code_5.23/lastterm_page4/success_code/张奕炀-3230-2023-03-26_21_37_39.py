list1 = eval(input())
list2 = list(range(len(list1)))
for i in range(len(list1)):
    max_number = list1.pop(list1.index(max(list1)))
    list2[i] = max_number
for i in range(len(list2)):
    list2[i] = str(list2[i])
string = ''.join(list2)
answer = int(string)
print(answer)
