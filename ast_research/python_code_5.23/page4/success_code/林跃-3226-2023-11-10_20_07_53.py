def search(nums):
    x=''
    for i in nums:
        if nums.count(i)>len(nums)//2:
            x=x+i
    return x





nums = eval(input())
y = search(nums)
print(y)


