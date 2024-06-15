ls=eval(input())
def is_prime(num):
    for i in range(2,num):
        if i ==0:
            return False
    list=[]
    for num in ls:
        if is_prime(num):
            is_prime(num).append(num)
print(list)

