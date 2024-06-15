list_1 =list(eval(input()))
str_1=""

for i in range(len(list_1)):

    int_max =max(list_1)
    list_1.remove(int_max)
    str_1 =str_1 + str(int_max)
print(str_1)

