'''读入一个整数列表，把数值为0的元素移动到列表尾部，其他元素的相对顺序不变。输出调整后的列表。
【输入形式】
按照列表的形式输入，包括方块号，逗号分隔。
【输出形式】
直接使用print打印
【样例输入】
[1,0,2,0,3,0,4]
【样例输出】
[1, 2, 3, 4, 0, 0, 0]
'''
list1=eval(input())
a=list1.count(0)
list1.remove(0)
for i in range(a):
    list1.remove(0)
    list1.append(0)
print(list1,sep=" ")
