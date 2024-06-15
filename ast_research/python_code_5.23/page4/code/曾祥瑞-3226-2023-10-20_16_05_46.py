def search(nums):
    a=0
    for x in nums:
        if nums.count(x)>a:
            a=nums.count(x)
    b=len(nums)
    if a>b//2:
        return a
    else:
        search(nums)=False





nums = eval(input())
y = search(nums)
print(y)


