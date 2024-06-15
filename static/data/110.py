__name__ = input("请输入一个字符串：")
name1 = 0
name2 = 0
name3 = 0
name4 = 0
lst = list(__name__)
for i in range(len(lst)):
    if lst[i].isdigit():
        name1 += 1
    elif lst[i].isalpha():
        name2 += 1
    elif lst[i] == " ": 
        name3 += 1
    else:
        name4 += 1

result = [str(name1), str(name2), str(name3), str(name4)]
print(" ".join(result))
#使用 str.join() 方法时，你应该传递一个可迭代对象作为参数，而不是单独的几个参数。