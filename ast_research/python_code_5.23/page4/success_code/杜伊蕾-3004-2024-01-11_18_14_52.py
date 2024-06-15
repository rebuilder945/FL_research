'''a=eval(input())
b=[]
for i in a:
    if i>=2:
        for j in range(2,i,1):
            if i%j==0:
                break
        else:
             b.append(i)
print(b)'''
a=eval(input())
b=[]
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
for i in a:
    if is_prime(i)==True:
        b.append(i)
print(b)

