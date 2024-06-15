lista = eval(input())
prime_list = []
for num in lista:    
    if num == 2 or num == 3:        
        prime_list.append(num)    
    elif num > 3:        
        is_prime = True        
        for i in range(2, int(num**0.5) + 1):  
            if num % i == 0:               
                 is_prime = False               
                 break       
            if is_prime:           
                prime_list.append(num)
print(prime_list)



