a=eval(input())
list=[]
for i in a:
    if i not in list:
        list.append(i)
    else:
        list.remove(i)
        list.append(i)
print(list)
