def search(nums):
    n = len(nums)
    count = {}
    for num in nums:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1
        if count[num] > n // 2:
            return num
    return False





nums = eval(input())
y = search(nums)
print(y)


