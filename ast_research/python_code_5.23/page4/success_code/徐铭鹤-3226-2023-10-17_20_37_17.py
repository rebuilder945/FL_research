def search(nums):
       for i in range(nums):
             n=len(nums)
             if nums.count(i)>n//2:
                 print(i)
             else:
                   print(False)
           





nums = eval(input())
y = search(nums)
print(y)


