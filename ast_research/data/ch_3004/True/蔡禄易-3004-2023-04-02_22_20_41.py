def get_prime(num):
    if num<=1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
a = eval(input())
lst = []
haha = []
for i in a:
    if get_prime(i) == 0:
        haha.append(i)
    else:
        lst.append(i)
print(lst)

