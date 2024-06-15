Nums=eval(input())
n=max(Nums)
for i in Nums:
    for x in range(2,n):
        if i%x==0:
            Nums.remove(i)
            print(Nums)
