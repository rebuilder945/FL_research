def search(nums):
    for i in nums:
        if nums.count(i) >n//2:
            a = i
        else:
            print("False")
    return a





nums = eval(input())
y = search(nums)
print(y)


