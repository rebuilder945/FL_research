def search(nums):
    for x in nums:
        a=count(x)/len(nums)
        if a>len(nums)/2:
        return x
        else:
        return False





nums = eval(input())
y = search(nums)
print(y)


