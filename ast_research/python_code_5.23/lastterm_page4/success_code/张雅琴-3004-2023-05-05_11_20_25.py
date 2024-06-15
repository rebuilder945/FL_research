import math
lst=eval(input())
def prime(i):
    for x in range(2,int(math.sqrt(i))+1):
        if i!=2 and i % x==0:
            return False
    return True
for i in lst:
    lst1=[]
    if prime(i):
        lst1.append(i)
    elif i==2:
        lst1.append(i)
print(lst1)
            
