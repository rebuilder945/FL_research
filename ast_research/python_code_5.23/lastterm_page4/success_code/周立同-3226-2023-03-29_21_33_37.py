def search(nums):
    for a in nums:
        if nums.count(a)>len(nums)//2:
            b=a
    if b:
        return b
    else:
        return "False"





nums = eval(input())
y = search(nums)
print(y)


