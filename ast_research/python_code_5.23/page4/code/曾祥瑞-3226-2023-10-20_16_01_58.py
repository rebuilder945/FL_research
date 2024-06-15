def search(nums):
    a=0
    for x in nums:
        if nums.count(x)>a:
            a=nums.count(x)
    if a>(nums.len())//2
        return a
    else:
        search(nums)=False





nums = eval(input())
y = search(nums)
print(y)


