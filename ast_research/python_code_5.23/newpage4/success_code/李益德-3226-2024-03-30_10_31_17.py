def search(num):
    nums=list(num)
    a=0
    for i in nums:
        if nums.count(i)>len(nums)/2:
            
            a+=1
            return i
    if a ==0:
        return False






nums = eval(input())
y = search(nums)
print(y)


