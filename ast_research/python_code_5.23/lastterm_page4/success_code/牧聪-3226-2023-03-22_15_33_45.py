def search(nums):
    n = len(nums)
    counts = {}
    degree = 0
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
        if counts[num] > degree:
            degree = counts[num]
            mode = num
    if degree > n // 2:
        return mode
    else:
        return False






nums = eval(input())
y = search(nums)
print(y)


