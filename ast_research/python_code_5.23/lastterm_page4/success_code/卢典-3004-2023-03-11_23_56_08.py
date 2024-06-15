Nums=eval(input())
for i in Nums:
    for x in range(2,i):
        if i%x==0:
            Nums.remove(i)
            print(Nums)
            
