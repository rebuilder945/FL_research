list=eval(input())
for i in list.copy():
    if list.count(i)>1:
        list.remove(i)
print(list)

