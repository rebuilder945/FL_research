def maxsum(nums):
    import random
    list = []
    a = 0
    while a < len(nums):
        list.append([])
        a += 1    
    list1 = []
    index = random.randint(0,len(nums)-1)
    for i in nums:
        while len(list[index]) < 2:
            list[index].append(i)
    for i in list:
        list1.append(min(list[index]))
    return sum(list1)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

