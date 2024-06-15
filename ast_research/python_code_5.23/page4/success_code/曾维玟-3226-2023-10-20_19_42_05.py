def search(nums):
      for x in nums:
            if nums.count(x)>len(nums)%2:
                print(x)
            
                





nums = eval(input())
y = search(nums)
print(y)


