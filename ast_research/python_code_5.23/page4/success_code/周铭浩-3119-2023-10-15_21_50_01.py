list=eval(input())
for x in list:
    if list.count(x)>1:
        list.remove(x)
    else:
        continue
print(list)
