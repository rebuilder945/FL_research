def search(nums:list):
    n=len(nums)
    for i in nums:
        x = nums.count(i)
        if x>n//2:
            h=i
        else:
            h='False'
    return h





nums = eval(input())
y = search(nums)
print(y)


