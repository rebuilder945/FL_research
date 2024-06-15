import math
lst=eval(input())
def prime(i):
    for x in range(2,int(math.sqrt(i))+1):
        if i!=2 and i % x==0:
            return False
        elif i==2:
            return True
    return True
for i in lst:
    lst1=[]
    if prime(i):
        lst1.append(i)
print(lst1)
            
