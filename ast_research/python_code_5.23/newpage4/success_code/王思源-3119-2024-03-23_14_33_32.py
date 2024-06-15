list = eval(input())

index = []
for i in range(len(list)):
    if(list.count(list[i]) != 1):
        index.append(list[i])

for i in range(len(index)):
    if(list.count(index[i]) != 1):
        list.remove(index[i])

print(list)
