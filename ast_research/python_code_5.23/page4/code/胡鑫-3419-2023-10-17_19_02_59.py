def calDegrees(nums)
       list 2:[ ]
       for x in nums:
             a=nums.count(x)
             list 2.append(a)
       return max (list2)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

