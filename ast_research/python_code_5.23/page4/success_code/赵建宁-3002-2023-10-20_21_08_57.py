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
if 0 in is_prime:
    is_prime.remove(0)
if 1 in is_prime:
    is_prime.remove(1)
print(is_prime)

