def search(nums:list):
    c=len(nums)/2
    s=False
    for x in nums:
        if nums.count(x)>c:
            s=x





nums = eval(input())
y = search(nums)
print(y)


