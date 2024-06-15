def search(nums):
    for x in nums:
        a=nums.count(x)
        b=len(nums)/2
        if a>b:
            return(x)
        else:
            return 'False'





nums = eval(input())
y = search(nums)
print(y)


