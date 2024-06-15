Nums=eval(input())
Num=Nums.remove(0,1)
for i in Nums:
    for x in range(2,i):
        if i%x==0:
            Num.remove(i)            
print(Num)
