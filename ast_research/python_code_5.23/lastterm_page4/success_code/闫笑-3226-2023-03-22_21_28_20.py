def search(nums):
      for x in range(nums):
           if nums.count(x)>n/2:
              y=x
           else:
               print(False)





nums = eval(input())
y = search(nums)
print(y)


