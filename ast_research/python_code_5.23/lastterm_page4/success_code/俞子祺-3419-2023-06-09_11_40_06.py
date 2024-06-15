def calDegrees(nums):
    m=0
    ls=[]
    for x in nums:
        m=nums.count(x)
        ls.append(m)
    ls.sort()
    return(ls[-1])
        



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

