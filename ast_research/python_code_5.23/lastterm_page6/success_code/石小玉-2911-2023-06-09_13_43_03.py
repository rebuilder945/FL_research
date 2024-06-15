n=list(input())
nums=[]
for i in n:
    x=(i+5)%10
    nums.append(x)
nums=nums[::-1]
for x in nums:
    print(x,end="")
