def calDegrees(nums):
        b=0
        for i in range(len(nums)):
                s=nums[i]
                a=nums.count(s)
                if a>=b:      
                        b=a
                else:
                        pass
        return b
          


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

