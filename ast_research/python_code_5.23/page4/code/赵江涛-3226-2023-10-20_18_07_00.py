def search(nums):
  count = {} f
  or num in nums: if num in count:
   count[num] += 1 
  else: count[num] = 1

 for num, freq in count.items():
    if freq > len(nums) // 2:
        return num

return False






nums = eval(input())
y = search(nums)
print(y)


