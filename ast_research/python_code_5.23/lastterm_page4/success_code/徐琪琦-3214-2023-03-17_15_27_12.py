#读入一个整数列表，把数值为0的元素移动到列表尾部，其他元素的相对顺序不变。输出调整后的列表
list1 = eval(input())
num = list1.count(0)        
for i in range(list1.count(0)):    #十进制数字不允许出现023这种开头为0的
    list1.remove(0)
    i += 1
for x in range(i):
    list1.append(0)
    x += 1
print(list1)
