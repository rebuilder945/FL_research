def maxsum(nums):
      nums.reverse()
      2n=len(nums)
      b=[]
      for i in range(1,2,2n-1):
            b.append(nums(i))
      c=sum(b)
     return c
            
            




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

