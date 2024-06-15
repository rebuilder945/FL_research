def search(nums):
       n = int(len(nums)/2)
       for i in nums:
             if nums.count(i)>n:
                  print(i)
                  break
             else:
                  print("False")
                  break





nums = eval(input())
y = search(nums)
print(y)


