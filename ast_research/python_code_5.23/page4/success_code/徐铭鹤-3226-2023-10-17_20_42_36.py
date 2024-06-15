def search(nums):
       for i in range(len(nums)):
             n=len(nums)
             if nums.count(i)>n//2:
                 a=i
             else:
                  a="false"
             return a





nums = eval(input())
y = search(nums)
print(y)


