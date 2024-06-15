ls=[]
def calDegrees(nums):
    for x in nums:
        count=nums.count(x)
        ls.append(count)
    result=max(ls)
    return result



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

