nums=eval(input())
avg=sum(nums)/len(nums)
b=int(avg)
if avg>b:
    print("%.2f"%avg)
else:
    print(b)
