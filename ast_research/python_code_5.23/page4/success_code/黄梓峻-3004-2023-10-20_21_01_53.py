def prime(num):
    if num<2:
        return False
    for i in range(2,int(num** .5)+1):
        if num % i == 0:
            return False
    return  True
num_list=list(map(int,input()))
prime_list=[]
for num in num_list:
    if num in prime(num):
        prime_list.append(num)
print(prime_list)
