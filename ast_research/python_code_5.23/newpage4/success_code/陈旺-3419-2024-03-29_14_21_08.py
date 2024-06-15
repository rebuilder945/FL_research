def calDegrees():
    n=[]
    for i in nums:
        n.append(nums.count(i))
    return(max(n))


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

