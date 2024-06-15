def calDegrees(nums):
    count={}
    m=0
    for i in nums:
        if not i in count:
            count[i] = 1
        else:
            count[i] += 1    
    m=max(m,count[i])        
    return m


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

