list_1 =input().split(",")
list_2 =list(eval(input()))
list_3 =[]

for i in range(len(list_1)):
    list_4 =[]
    list_4.append(list_1[i])
    list_4.append(list_2[i])
    list_3.append(list_4)
print(list_3)

