list1 = input()
list2 = eval(input())
list3 = list(list1)
new = []

for i in range(len(list2)):
    element = str(list3[i:i+1]) + "," + str(list2[i])
    #移除额外的引号,确保字符串拼接时不会混淆字节字符串和普通字符串
    list5 = eval("[" + element + "]")
    new.append(list5)

print(new)