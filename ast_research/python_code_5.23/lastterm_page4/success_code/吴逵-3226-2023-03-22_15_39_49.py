def search(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    
    count = 0
    for num in nums:
        if num == candidate:
            count += 1
            
    return candidate if count > len(nums) // 2 else False






nums = eval(input())
y = search(nums)
print(y)


