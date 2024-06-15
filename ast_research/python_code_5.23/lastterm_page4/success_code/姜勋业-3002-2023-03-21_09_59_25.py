nums=eval(input())
k=sum(nums)/len(nums)
if type(k)==int:
    print(int(k))
else:
    print("%.2f"%k)
