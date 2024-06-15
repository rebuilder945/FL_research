nums=eval(input())
def is_prime(num):
    if num<=1:
        print('False')
    for i in range(2,int(num**0.5)+1):
        if num % i==0:
            print('False')
prime_numbers=[num for num in nums if is_prime(num)]
print(is_prime)
