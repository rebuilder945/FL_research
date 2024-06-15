def maxsum(list):
    list.sort()
    n = []
    for x in list:
        if list.index(x)%2 == 0:
            n.append(x)
    return sum(n)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

