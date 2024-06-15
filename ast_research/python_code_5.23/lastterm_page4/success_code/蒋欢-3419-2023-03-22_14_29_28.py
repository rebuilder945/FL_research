def calDegrees(nums):
    result=[]
    times=[]
    for i in nums:
        if i not in result:
            result.append(i)
            times.append(nums.count(i))
        else:
            pass
    n=max(times)
    return n


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

