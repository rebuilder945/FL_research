n=eval(input())
rabbit=[1,1]
sum=0
while n>0:
    new=rabbit[-1]+rabbit[-2]
    rabbit.append(new)
    fenshu=rabbit[-1]/rabbit[-2]
    sum+=fenshu
    n-=1
print("%.4f"%(sum))
