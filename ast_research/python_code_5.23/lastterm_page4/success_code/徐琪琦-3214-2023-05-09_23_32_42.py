#读入一个整数列表，把数值为0的元素移动到列表尾部，其他元素的相对顺序不变。输出调整后的列表
list1 = eval(input())   #即使输入的是【1，2，3】,list1也还是str因为input出来的就是str
a = list1.count(0) #count只能用于str
for i in range(a):           #十进制数字不允许出现023这种开头为0的
    list1.remove(0)
    i += 1
for x in range(a):           #不可以不设a，就直接for x in range(i),i不是全局变量
    list1.append(0)
    x += 1
print(list1)
