nums=eval(input())
list=[]
for x in nums and i in range(2,x-1):
    if x!=0 and x!=1 and x%i!=0:
        list.append(x)
    else:
        pass
print(list)
