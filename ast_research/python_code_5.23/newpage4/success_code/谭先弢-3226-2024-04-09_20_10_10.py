def search(nums):
    L = len(nums)/2
    for x in nums:
        if nums.count(x) > L:
            return(x)
            break
    else:
        return('False')





nums = eval(input())
y = search(nums)
print(y)


