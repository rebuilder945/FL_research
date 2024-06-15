def calDegrees(nums):
       lst = [ ]
       for x in nums:
             a=nums.count(x)
             lst.append(a)
       return max (lst)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

