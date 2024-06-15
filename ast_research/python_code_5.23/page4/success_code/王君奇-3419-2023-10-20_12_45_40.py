def find_degree(nums):
     counts={}
     for num in nums:
          count[num]=counts.get(num,0)+1
degree=max(counts.values())


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

