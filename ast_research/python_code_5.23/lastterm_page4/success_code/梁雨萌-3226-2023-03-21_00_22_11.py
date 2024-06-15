def search(nums):
    m=len(nums)//2
    num="False"
    for i in range(0,len(nums)):
        f=nums.count([i])
        if  f>m:
            num=nums[i]
            break
    return(num)





nums = eval(input())
y = search(nums)
print(y)


