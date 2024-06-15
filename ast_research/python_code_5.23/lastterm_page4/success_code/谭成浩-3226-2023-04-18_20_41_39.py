n=[]
def search(nums):
    for i in nums:
        n.append(nums.count(i))
    m=max(n)
    if m>len(nums)/2:
        for i in nums:
            if nums.count(i)==m:
                return i
                Done
    else:
        return 'False'
     
   





nums = eval(input())
y = search(nums)
print(y)


