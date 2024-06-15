def search(nums,x):
x=0
for n in nums:
    x+=1
if x>n//2:
    return x
else:
    print(False)

   
        





nums = eval(input())
y = search(nums)
print(y)


