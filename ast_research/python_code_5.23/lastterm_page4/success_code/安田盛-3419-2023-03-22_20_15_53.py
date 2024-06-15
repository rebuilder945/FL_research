def calDegrees(nums:list):
    m=[]
    for x in nums:
        temp = nums.count(x)
        if temp not in m:
            m.append(temp)
    return max(m)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

