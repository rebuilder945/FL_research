def search(nums):
    n=len(nums)
    for i in nums:
        if nums.count(i)>n/2:
            print(i)
        else:
            print("False")






nums = eval(input())
y = search(nums)
print(y)


