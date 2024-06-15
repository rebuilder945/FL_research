def search(nums:list):
    for x in nums:
        a=nums.count(x)
        if a>len(nums)/2:
            print(x)
        else:
            print(False)





nums = eval(input())
y = search(nums)
print(y)


