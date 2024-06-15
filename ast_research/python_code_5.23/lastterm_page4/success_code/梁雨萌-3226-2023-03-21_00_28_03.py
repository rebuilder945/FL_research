def search(nums):
    m=len(nums)//2
    for i in range(0,len(nums)):
        f=nums.count(nums[i])
        if  f>m:
            num=nums[i]
            break
        else:
            num="False"
    return(num)





nums = eval(input())
y = search(nums)
print(y)


