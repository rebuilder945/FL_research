def search(nums,n):
      n = len(nums)
      b = n//2
      for i in range(nums):
           if count(i) > b:
                return i
           else:
                print("False")





nums = eval(input())
y = search(nums)
print(y)


