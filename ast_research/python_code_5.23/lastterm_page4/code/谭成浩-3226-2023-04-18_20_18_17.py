def search(nums):
     for i in nums:
        if nums.count(i)>len(nums)/2:
            n=i
    if n ==None:
        return 'false'
    else:
        return n





nums = eval(input())
y = search(nums)
print(y)


