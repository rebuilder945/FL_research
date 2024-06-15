def maxsum(nums):
       nums.sort()
       s=[]
       n=len(nums)
       for i in range(0,n+,2):
            s.append(nums[i])
  
       return(sum(s))
       




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

