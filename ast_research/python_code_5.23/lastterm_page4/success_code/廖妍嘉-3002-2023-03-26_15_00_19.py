nums=eval(input())
a=sum(nums)/len(nums)
if a-int(a)>0:
    print("%.2f"%a)
else:
    print(int(a))
