def search(nums):
    for x in nums:
        b = nums.count(x)
        n = len(nums)
        if b > (n//2):
            print(x)
        else:print("False")





nums = eval(input())
y = search(nums)
print(y)


