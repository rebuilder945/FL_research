list_1 =list(eval(input()))
for i in list_1:
    if i ==0:
        list_1.remove(i)
        list_1.append(0)
print(list_1)
