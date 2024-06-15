def search(nums):
    x=0
    for i in range (len(nums)):
        a=nums.count(nums[i])
        if a >len(nums)/2:
            x+=1
        else:
            pass
    if x==1:
        return a    
    else: 
        return False





nums = eval(input())
y = search(nums)
print(y)


