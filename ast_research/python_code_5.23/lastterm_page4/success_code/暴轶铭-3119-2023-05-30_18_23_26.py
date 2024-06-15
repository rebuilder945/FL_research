#输入一个列表，删除其中的重复值，再输出。
#要求：假设列表中存在k个值为a的元素，删除前k-1个元素，保留最后一个。 不同元素在列表中的相对位置不应被改变。
lst = eval(input())
result = []
for x in lst:
    if x not in result:
        result.append(x)
print(result)
