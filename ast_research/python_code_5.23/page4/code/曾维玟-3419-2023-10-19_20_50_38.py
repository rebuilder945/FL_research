def calDegrees(nums):
      ls2 = [ ]
      for x in nums:
           wi = nums.count(x)
            ls2.append(wi)
      return max(ls2)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

