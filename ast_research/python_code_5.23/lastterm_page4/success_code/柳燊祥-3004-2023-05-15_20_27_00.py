nums=eval(input())
list=[]
def p(x):
    f=True
    i=2
    while i<=x:
        if x%i==0:
         f=False
         break
    i=i+1
    return f
for x in nums:
    if x!=0 and x!=1 and p(x)==True:
        list.append(x)
    else:
        pass
print(list)
