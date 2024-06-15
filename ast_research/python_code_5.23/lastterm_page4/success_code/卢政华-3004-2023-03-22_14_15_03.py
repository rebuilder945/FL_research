def get_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False 

ls = input()
is_prime = []
not_prime = []
for i in ls:
    if get_prime(i) == False:
        not_prime.append(i) 
    else:
        is_prime.append(i)  
print(is_prime)
