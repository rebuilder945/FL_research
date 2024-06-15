def search(nums):
    n=max(nums.count())
    if n>len(nums):
        return n
    else:
        return 'false'
     
   





nums = eval(input())
y = search(nums)
print(y)


