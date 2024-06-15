nums=eval(input())
a=nums.count(0)
if a==0:
    print(nums)
else:
    i=0
    while a>i:
        nums.remove(0)
        nums.append(0)
        i+=1
    print(nums)

