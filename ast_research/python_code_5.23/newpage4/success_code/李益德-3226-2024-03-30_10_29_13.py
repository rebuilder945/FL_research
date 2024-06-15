def search(num):
    nums=list(num)
    a=0
    for i in nums:
        if nums.count(i)>len(nums)/2:
            print(i)
            a+=1
    if a ==0:
        print("False")





nums = eval(input())
y = search(nums)
print(y)


