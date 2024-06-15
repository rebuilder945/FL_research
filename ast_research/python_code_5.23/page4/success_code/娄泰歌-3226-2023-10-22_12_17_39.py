def majority_element2(nums):
      n = len(nums)

      for y in nums:
           count = sum(1 for element in nums if element == y)
           if count >= math.ceil(n/2):
                return i





nums = eval(input())
y = search(nums)
print(y)


