for num in nums:
    count[num]=count.get(num,0)+1
    degree=max(count.values())
    
  


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

