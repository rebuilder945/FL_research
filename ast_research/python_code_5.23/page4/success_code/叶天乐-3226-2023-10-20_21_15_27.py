def search(nums):
    for x in nums:
        if [nums].count(x)>len(nums)//2:
            print(x)
        else:
            print(False)






nums = eval(input())
y = search(nums)
print(y)


