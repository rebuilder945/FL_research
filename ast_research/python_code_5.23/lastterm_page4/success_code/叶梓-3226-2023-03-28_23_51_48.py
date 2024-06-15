def search(nums):
    n=len(nums)
    count = {}
    for num in nums:
        count[num] = count.get(num,0) + 1
        if count[num] > n//2:
            return num
    if count[num] < n//2:
        return False





nums = eval(input())
y = search(nums)
print(y)


