def maxsum(nums):
        s=len(nums) 
        a=[]
        b=0
        for i in range(1,s,2):
                m=nums[i]
                b+=m
                
        
        return b




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

