def caldegrees(nums):
    s=list(nums)
    t=(s.count(max(s,key=s.count)))
    return t
    


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

