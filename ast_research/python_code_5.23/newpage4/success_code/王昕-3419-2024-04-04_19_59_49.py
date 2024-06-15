nums=eval(input())
a=[]
for i in nums:
    n=nums.count(i)
    a.append(n)
b=max(a)
print(b)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

