def find degree(nums):
      count=[]
       for num in nums:
         counts[num]=counts.get(num,0)+1
       degree=max(counts.values())
        renturn degree


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

