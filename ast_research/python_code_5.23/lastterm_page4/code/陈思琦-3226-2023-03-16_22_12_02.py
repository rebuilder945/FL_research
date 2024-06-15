def y(nums):
search=i
    N=len(nums)//2
    for i in nums:
        if nums.count(i)>=N:
            return search
        else:
            print(False)





nums = eval(input())
y = search(nums)
print(y)


