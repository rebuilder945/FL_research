def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
a=eval(input())
n1=[]
n2=[]
for i in a:
    if i==1 or i==0:
        n1.append(i)
    elif prime(i)==False:
        n1.append(i)
    else:
        n2.append(i)
print(n2)
