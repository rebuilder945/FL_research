def get_prime(num):
    if ls.count(num) == 1:
        return True
    else:
        return False
ls=eval(input())
not_prime = []
is_prime = []
for i in ls:
    if get_prime(i) == False:
        not_prime.append(i)
    else:
        is_prime.append(i)
a = is_prime[0:]
a.sort()
print(*a,sep=',')
