def maxsum(list1):
    list1.sort()
    sum = 0
    for i in range(len(list1)):
        if i % 2 == 0:
            sum = sum + list1[i]  # 此处应该是 list1[i] 而不是 list[i]
    return sum
#在 maxsum 函数中，代码块没有正确对齐，Python 对缩进非常敏感，缩进必须一致，否则会导致 IndentationError 错误。

nums = eval(input())
v = maxsum(nums)  # 调用自定义函数
print(v)
