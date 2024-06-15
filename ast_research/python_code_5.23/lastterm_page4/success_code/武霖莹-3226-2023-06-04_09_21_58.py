def search(nums):
    lst = []
    for i in nums:
        x = nums.count(i)
        lst.append(x)
    max1 = max(lst)
    if max1 > len(nums)//2:
        return max1
    else:
        return False





nums = eval(input())
y = search(nums)
print(y)


