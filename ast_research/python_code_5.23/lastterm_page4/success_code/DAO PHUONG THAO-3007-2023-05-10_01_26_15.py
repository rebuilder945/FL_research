def maxsum(nums:list):
    nums.sort()#省序排列，每两个一对
    minv=nums[::2] # 通过切片取出每一对的最小值
    sumv=sum(minv) # 计算最小值的和
    return sumv

nums  =  eval(input()) 
v  =  maxsum(nums)#调用自定义函数 
print(v)
