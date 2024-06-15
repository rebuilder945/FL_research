def search(nums):
    """
    :type nums: List[int]
    :rtype: int|False
    """
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    if nums.count(candidate) > len(nums) // 2:
        return candidate
    else:
        return False






nums = eval(input())
y = search(nums)
print(y)


