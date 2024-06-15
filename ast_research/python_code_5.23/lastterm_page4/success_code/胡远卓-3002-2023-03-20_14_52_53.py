nums=eval(input())
res=sum(nums)/len(nums)
if res==int(res):
    print(int(res))
else:
    print("%.2f"%(res))
