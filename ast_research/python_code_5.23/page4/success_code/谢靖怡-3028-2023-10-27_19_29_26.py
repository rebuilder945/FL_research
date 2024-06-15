nums=input().split(",")
ls=list(nums)
a=eval(ls[0])
b=eval(ls[2])
c=eval(ls[1])
ls1=[a]
for i in range(1,c-1):
    d=a+i*b
    ls1.append(d)
print(ls1)
