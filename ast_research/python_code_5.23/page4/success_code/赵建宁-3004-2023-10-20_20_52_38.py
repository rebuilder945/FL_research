r1 = eval(input())
is_prime = []
not_prime = []
def get_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
for i in r1:
    if get_prime(i) == False:
        not_prime.append(i)
    else:
        is_prime.append(i)
print(is_prime)

