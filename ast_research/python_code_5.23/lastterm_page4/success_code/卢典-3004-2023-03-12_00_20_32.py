Nums=eval(input())
if 0 in Nums:
    Nums.remove(0)
if 1 in Nums:
    Nums.remove(1)
for i in Nums:
    for x in range(2,i):
        if i%x==0:
            Ans=[i]
            Nums=[n for n in Nums not in Ans ]
print(Nums)
