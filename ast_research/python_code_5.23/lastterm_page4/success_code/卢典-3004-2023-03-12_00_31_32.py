def prime(Nums):
    for i in Nums:
        for j in range(2,i):
            if i%j==0:
                break
            else:
                Nums=(i)
                return(Nums)
Nums=eval(input())
Ans=prime(Nums)
print(Ans)
