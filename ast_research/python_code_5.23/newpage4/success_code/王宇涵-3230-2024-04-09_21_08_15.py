nums= eval(input())
nums.sort(reverse=True)
for x in nums:
    if x[0]==x[1]==0:
        print(0)
        break 
    else:
        print(x,end='')

