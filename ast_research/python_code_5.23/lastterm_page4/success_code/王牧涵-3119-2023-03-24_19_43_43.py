list= eval(input())
list.reverse()
list2=['']
for i in list:
    if i not in list2:
        list2.insert(0,i)
list2.pop()
print(list2)

