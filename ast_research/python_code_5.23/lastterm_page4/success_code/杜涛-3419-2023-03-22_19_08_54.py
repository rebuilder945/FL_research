def calDegrees(nums):
      a=[]
      for i in nums :
            n=nums.count(i)
            if n not in a:
                 a.append(n)
      return max(a)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

