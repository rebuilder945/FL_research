nums=eval(input())
k=sum(nums)/len(nums)
if type(k)==int:
    print(k)
else:
    print("%.2f")%(k)
