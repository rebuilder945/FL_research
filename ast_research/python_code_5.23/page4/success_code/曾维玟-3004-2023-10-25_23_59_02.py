def is_prime(num):
    if num < 2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
        return True
input_list = eval(input()) 
output_list = [num for num in input_list if is_prime(num)]  
print(output_list) 
