def search(n):
      for i in nums:
            if nums.count(i)>len(nums)//2:
               n=i
            else:
               print('False')
       return n





nums = eval(input())
y = search(nums)
print(y)


