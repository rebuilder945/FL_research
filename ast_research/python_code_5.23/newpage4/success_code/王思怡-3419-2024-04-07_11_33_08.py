a = []
def calDegrees(nums):
    for i in nums:
         a.append(count(i))
    d = max(a)
    return d



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

