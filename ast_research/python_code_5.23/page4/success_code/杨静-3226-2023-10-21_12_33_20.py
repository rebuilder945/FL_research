def search(nums):
    n=len(nums)//2
    for x in nums:
        if nums.count(x)>n:
            return x
            break
        else:
            print("False")





nums = eval(input())
y = search(nums)
print(y)


