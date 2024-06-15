
def is_prime(num):
    if num<2:
        return False
        for i in range(2,int(num**0.5)+1):
            if num % i ==0:
                return False
            return True
def find_prime_numbers(numbers):
            prime_numbers=[]
            for num in numbers:
                if is_prime(num):
                    prime_numbers.append(num)
                    return prime_numbers
numbers=eval(input())
prime_numbers=find_prime_numbers(numbers)
print(prime_numbers)
