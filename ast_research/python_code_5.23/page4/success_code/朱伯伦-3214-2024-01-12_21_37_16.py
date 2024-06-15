list=eval(input())
for i in range(len(list)):
    if list[i]==0:
        list.append(list.pop(i))
print(list)
