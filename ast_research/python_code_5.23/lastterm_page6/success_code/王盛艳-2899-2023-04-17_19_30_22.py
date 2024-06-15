n,m = input().split(" ")
n = int(n)
m = int(m)
nums = []
nums1 = []
if (m<n) or (m-n) < 3 or m<0 or n<0 or n>8:
    print("illegal input")
else:
    for x in range (n,m):
        nums.append(x)
    for x in range(len(nums)):
        for y in range(len(nums)):
            for z in range(len(nums)):
                if x!=y and y!=z and x!=z and nums[x]!=0:                   
                    s1=str(nums[x])+str(nums[y])+str(nums[z])
                    if s1 not in nums1:
                        nums1.append(s1)
                    else:
                        pass
                else:
                    pass
    for y in nums1:
        y=int(y)
        print("%d "%y,end="")
