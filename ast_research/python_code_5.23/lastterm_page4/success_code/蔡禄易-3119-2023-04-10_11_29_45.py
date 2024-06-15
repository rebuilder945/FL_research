a = eval(input())
a = a.reverse()
list1 = []
for i in a:
    if i not in list1:
        list1.insert(0,i)
print(list1)

