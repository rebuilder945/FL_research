def search(nums):
    n=len(nums)
    for x in nums:
        if nums.count(x)<=n//2:
            continue
        else:
            a=x
            if a is not None:
                a=a
                return a
            else:
                print('False')





nums = eval(input())
y = search(nums)
print(y)


