def calDegrees(nums):
      dic={}
    for i in nums:
    if i not in dic:
        dic[i]=1
     if i in dic:
         dic[i]+=1
return maxdic


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

