def search(num):
    nums=list(num)
    a=0
    for i in nums:
        if nums.count(i)>len(nums)/2:
            
            a+=1
    if a ==0:
        print("False")
    return i






nums = eval(input())
y = search(nums)
print(y)


