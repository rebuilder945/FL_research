def maxsum(nums):
    nums1=[]
    d=int(len(nums)/2)-1
    numssorted=sorted(nums)
    for x in range(0,d):
        a=nums.pop(0)
        e=nums.pop(1)
        nums1.append(a)
    b=nums.pop(-2)
    v=sum(nums1)+b
    return v

    





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

