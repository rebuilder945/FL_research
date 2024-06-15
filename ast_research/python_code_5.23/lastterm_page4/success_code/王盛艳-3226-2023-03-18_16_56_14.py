def search(nums):
    s = 0
    n = len(n)
    for x in range(len(n)):
        if nums.count(x) > n/2:
            s = x
        else:
            s = False





nums = eval(input())
y = search(nums)
print(y)


