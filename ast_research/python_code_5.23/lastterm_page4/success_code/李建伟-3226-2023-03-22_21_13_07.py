def search(nums):
    lst = []
    for i in nums:
        x = nums.count(i)
        lst.append(x)
    max1 = max(lst)
    a = lst.index(max1)
    b = nums[a]
    if max1 > len(nums)//2:
        return b
    else:
        return False





nums = eval(input())
y = search(nums)
print(y)


