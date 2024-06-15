list = eval(input())
for i in list[:]:
    while list.count(i) > 1:
        list.remove(i)
print(list)            

