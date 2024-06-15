Nums=eval(input())
if 0 in Nums:
    Num=Nums.remove(0)
if 1 in Nums:
    Num=Nums.remove(1)
for i in Nums:
    for x in range(2,i):
        if i%x==0:
            Ans=[i]
            Num=[n*1 for n in Nums not in Ans ]
print(Num)
