def search(nums):
    counter = {}
    for num in nums:
        if num not in counter:
            counter[num] = 1
        else:
            counter[num] += 1
    max_num = 0
    max_count = 0
    for num, count in counter.items():
        if count > max_count:
            max_count = count
            max_num = num
    if max_count > len(nums) // 2:
        return max_num
    else:
        return False





nums = eval(input())
y = search(nums)
print(y)


