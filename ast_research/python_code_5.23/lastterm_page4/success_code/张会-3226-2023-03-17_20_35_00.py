def search(nums):
    a = len(nums)/2
    for i in range(len(nums)):
        if nums.count(i) >a:
            return i
        else:
            return False





nums = eval(input())
y = search(nums)
print(y)


