n=[]
def search(nums):
    for i in nums:
        n.append(nums.count(i))
    m=max(n)
    if m>len(nums)/2:
        return m
    else:
        return 'false'
     
   





nums = eval(input())
y = search(nums)
print(y)


