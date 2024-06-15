dic={}
nums=eval(input())
for i in nums:
    a=nums.count(i)
    dic[i]=a
print(max(dic.values()))


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

