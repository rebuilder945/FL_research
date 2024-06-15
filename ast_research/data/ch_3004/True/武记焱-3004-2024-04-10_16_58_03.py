def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
list1=eval(input())
list2=[]
for i in list1:
    if is_prime(i)==True:
        list2.append(i)
    else:
        pass
print(list2)
