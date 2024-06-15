nums=eval(input())
nums.sort(reverse=True)
if nums[0]==0:
    print(0)
else:
    ls1=[str(i)for i in nums]
    a=int("".join(ls1))
    print(a)
