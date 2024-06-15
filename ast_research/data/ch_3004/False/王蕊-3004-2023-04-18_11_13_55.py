def get_prime(num):
    for i in range(2,num):
        if num%i==0:
            return False
lst=eval(input())
is_prime=[]
for x in lst:
    if get_prime(x)==True:
        is_prime.append(x)
        

