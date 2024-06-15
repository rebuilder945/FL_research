def maxsum(nums):
    nums1=[]
    d=int(len(nums)/2)
    numssorted=sorted(nums)
    for x in range(0,d):
        c=numssorted.pop()
        nums1.append(c)
    b=min(nums)
    c=min(nums1)
    v=b+c
    return v

    





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

