def search(nums):
    b=len(nums)//2
    for i in nums:
        if nums.count(i)>b:
            a=i
        else: a=False
    return a





nums = eval(input())
y = search(nums)
print(y)


