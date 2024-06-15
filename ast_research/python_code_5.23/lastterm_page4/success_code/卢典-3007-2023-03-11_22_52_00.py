Nums=eval(input())
n,m=eval(input())
t=len(Nums)
if n<=m<=t :
    del Nums[n:m]
    print(Nums)
else:
    print("error")
