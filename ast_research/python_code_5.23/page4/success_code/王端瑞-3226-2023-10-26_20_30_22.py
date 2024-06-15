def search(nums):
    for i in nums:
        if nums.count(i)>len(nums)//2:
            y = i
            continue
        else:
            y = False






nums = eval(input())
y = search(nums)
print(y)


