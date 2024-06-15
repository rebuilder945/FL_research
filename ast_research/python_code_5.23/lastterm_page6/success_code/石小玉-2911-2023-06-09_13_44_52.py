n=list(input())
nums=[]
for i in n:
    x=(i+5)%10
    nums.append(int(x))
nums=nums[::-1]
for x in nums:
    print(x,end="")
