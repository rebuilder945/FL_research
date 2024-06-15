def search(nums):
    for x in nums:
        if nums.count(x)>len(nums)//2:
            bb=x
            break
    return bb





nums = eval(input())
y = search(nums)
print(y)


