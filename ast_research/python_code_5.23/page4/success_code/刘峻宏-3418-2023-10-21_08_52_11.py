def maxsum(nums):
        s=len(nums) 
        a=[]
        for i in range(s):
                m=nums[i]
                
                for x in range(s-1):
                        if x+i<=s-1:
                                n=nums[x+i]
                                y=m+n
                                a.append(y)
        a.sort()
        v=nums[len(a)]
        return v




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

