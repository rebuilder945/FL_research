ls=eval(input())
def is_prime(n): 
    for i in range(2, n): 
        if n == 0: 
            return False 
        return True

list_prime = [] 
for num in ls: 
    if is_prime(num): 
        list_prime.append(num)

print(list_prime)
