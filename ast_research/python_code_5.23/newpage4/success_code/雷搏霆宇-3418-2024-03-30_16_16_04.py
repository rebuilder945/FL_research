def maxsum(nums):
    b = []
    for i in nums:
        for x in nums:
            if i != x :
                b.append(min(i,x))
    print(max(b)+min(b))




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

