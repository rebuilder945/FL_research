#读入一个整数列表，把数值为0的元素移动到列表尾部，其他元素的相对顺序不变。输出调整后的列表。
nums = eval(input())
result = []
for i in nums:
    if i != 0:
        result.append(i)
    else:
        pass
for x in nums:
    if x == 0:
        result.append(x)
    else:
        pass
print(result)






