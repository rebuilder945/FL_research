list=input()
for i in range(len(list)):
    if list[i]==0:
        a=list.pop(i)
        list.append(a)
print(list)
