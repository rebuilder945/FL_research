def hua(x):
    nums=list(x)
    a=nums[0]
    b=nums[1]
    c=nums[2]
    x=a**3+b**3+c**3

n=int(input())
for x in range(n):
    if 100<x<1000 and hua(x):
        print(x)
    else:
        print("none")
