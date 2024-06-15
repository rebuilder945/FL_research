list_1 =list(eval(input()))
list_2 =[]
for i in list_1:
    
    if i in list_2:
        list_2.remove(i)
    list_2.append(i)
print(list_2)

