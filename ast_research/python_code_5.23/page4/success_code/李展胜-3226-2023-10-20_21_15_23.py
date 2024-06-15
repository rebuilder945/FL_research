def search(nums):
       for i in nums:
             if nums.count(i)>len(num)//2:
                 return i
             else:
                  return"False"





nums = eval(input())
y = search(nums)
print(y)


