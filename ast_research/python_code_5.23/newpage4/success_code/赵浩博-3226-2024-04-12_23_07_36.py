def search(nums):
    for i in nums:
        count=nums.count(i)
        n=len(nums)
        if count>(n//2):
          return i
        else:
            return False





nums = eval(input())
y = search(nums)
print(y)


