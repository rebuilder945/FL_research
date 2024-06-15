del calDegrees(nums):
    count={}
    for num in nums:
        if num in count:
            count[num]+=1
        else:
            count[num]=1
    maxn=max(count.values())
    return maxn


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

