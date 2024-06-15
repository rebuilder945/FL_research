def get_prime(num):
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
b = [1,0]
c = lst - b
print(c)

