def maxsum(nums):
        s=len(nums) 
        a=[]
        b=0
        nums.sort()
        for i in range(0,s,2):
                m=nums[i]
                b+=m
                
        
        return b




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

