def search(nums):
    count, y = 0, 0
    for i in nums:
        if i == y:
            count += 1
        else:
            if count == 0:
                y = i
                count = 1
            else:
                count -= 1
    return y






nums = eval(input())
y = search(nums)
print(y)


