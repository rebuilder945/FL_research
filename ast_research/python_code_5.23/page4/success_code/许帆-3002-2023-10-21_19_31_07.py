nums = eval(input())
b = sum(nums)/len(nums)
if b%1 == 0:
    print(int(b))
else:
    print("%.2f"%(b))
