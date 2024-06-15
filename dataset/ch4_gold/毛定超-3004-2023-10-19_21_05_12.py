def su(num):
    if num<=1:
        return False
    for i in range(2,num):
        if num%i==0 :
           return False



l1=eval(input())

l2=[]
for i in l1:
    if su(i)==False:
        continue
    else:
        l2.append(i)
print(l2)        






