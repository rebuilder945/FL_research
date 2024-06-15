def search(nums):
    for i in nums:
        if i＞len(nums)//2:
             return i
             break
        else:
             return False






nums = eval(input())
y = search(nums)
print(y)


