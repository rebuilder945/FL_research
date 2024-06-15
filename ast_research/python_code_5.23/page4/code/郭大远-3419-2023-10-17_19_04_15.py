def calDegrees(nums):
     d=[]
      for i in nums
        if i not in d:
         d[i]=1
        else:
         d[i]+=1
       return max(d)



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

