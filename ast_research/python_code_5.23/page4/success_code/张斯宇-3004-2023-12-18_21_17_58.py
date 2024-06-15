from math import sqrt
def is_prime(a):
    if(a<=2): 
        return True
    for i in range(2,int(sqrt(a)+1)):
        if(a%i==0):
            return False
    return True

lst=eval(input())
primelist=[]
for j in range(len(lst)):
    if(is_prime(lst[j])):
        primelist.append(lst[j])

print(primelist)

