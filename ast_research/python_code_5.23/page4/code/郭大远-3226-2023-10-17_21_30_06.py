def search(nums):
    n=len(nums)
    for i in nums:
        if nums.counts(i)>n//2:
            i=y
        else:
            print(False)
         return y





nums = eval(input())
y = search(nums)
print(y)


