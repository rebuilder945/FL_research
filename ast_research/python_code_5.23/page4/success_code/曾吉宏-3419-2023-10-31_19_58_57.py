nums = [1,2,3,3,4,5,4,3,3]
blanlis = []
for x in nums:
    m = nums.count(x)
    blanlis.append(m)
    pmax = max(blanlis)
print(pmax)



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

