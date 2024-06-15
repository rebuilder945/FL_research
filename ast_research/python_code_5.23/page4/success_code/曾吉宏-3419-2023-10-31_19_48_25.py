nums = [1,2,3,3,4,5,4,3,3]
b = []
for x in nums:
    m = nums.count(x)
    b.append(m)
    p = max(b)
print(p)



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

