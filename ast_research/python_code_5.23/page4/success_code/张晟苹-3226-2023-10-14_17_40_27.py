def search(n):
      for i in nums:
            if nums.count(i)>(len(nums))//2:
               n=i
            else:
               print('False')





nums = eval(input())
y = search(nums)
print(y)


