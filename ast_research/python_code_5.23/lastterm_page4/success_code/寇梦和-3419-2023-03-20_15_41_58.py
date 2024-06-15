def calDegrees(nums) :
    a=max(set(nums),key=nums.count)
    from collections import Counter
    b=Counter(a)
    return b


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

