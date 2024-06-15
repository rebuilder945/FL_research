def maxsum(nums):
    n2=len(nums)
    if n2==0 or n2==2:
        he=sum(nums)
    else:
        nums.sort()
        list=[]
        for i in range(n2):
            if i%2==0:
                a=nums[i]
                list.append(a)
        he=sum(list)
    return he





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

