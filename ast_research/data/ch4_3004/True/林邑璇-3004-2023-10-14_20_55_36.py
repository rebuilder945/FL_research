a=eval(input())
nums=[]
i=2
if 1 in a:
    a.remove(1)
if 0 in a:
    a.remove(0)
for i in a:
    j=2
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        nums.append(i)
print(nums)

