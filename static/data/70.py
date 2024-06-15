a = input()
b = eval(input())
list = a.split(",")
list3 = []

for x in list:
#在 for x in a: 循环中，使用的是字符串 a 而不是列表 list。将输入的字符串 a 拆分为列表 list。
    if x in b:
        list2 = [x, b.index(x)]
        list3.append(list2)
