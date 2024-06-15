nums= eval(input())
nums.sort(reverse=True)
for x in nums:
    if x==0:
        print(0)
    else:
        print(x,end='')

