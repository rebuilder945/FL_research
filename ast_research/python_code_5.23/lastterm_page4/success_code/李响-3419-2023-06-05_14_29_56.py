def calDegrees(nums) :
        b = []
        for x in nums:
         b.append(nums.count(x))
        return max(b)



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

