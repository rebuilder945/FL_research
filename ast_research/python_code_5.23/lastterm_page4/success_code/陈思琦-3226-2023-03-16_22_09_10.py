def y(nums):
    N=len(nums)//2
    for i in nums:
        if nums.count(i)>=N:
            nums=i
        else:
            print(False)





nums = eval(input())
y = search(nums)
print(y)


