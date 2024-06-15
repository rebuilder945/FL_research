def maxsum(nums):
    nums.sort()
    a=len(nums)/2
    d=[]
    for i in range(a):
        d.append(int(nums[i*2+1]))
    c=sum(d)
    return(c)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

