def search(nums):
    ls=[]
    a=len(nums)
    for i in nums:
       if nums.count(i)>a//2:
          ls.append(i)





nums = eval(input())
y = search(nums)
print(y)


