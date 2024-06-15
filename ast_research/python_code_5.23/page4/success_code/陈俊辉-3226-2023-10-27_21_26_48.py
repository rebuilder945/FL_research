def search(nums):
    n=len(nums)
    for i in nums:
        if count(i)>n/2:
            return i





nums = eval(input())
y = search(nums)
print(y)


