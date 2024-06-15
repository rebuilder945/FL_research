def search(nums):
    for x in nums:
        if nums.count(x)>2:
          return x
        else:
           pass





nums = eval(input())
y = search(nums)
print(y)


