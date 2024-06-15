# a=input()
# a=a.strip("[")
# a=a.rstrip("]")
# b=[int(i) for i in a.split(",")]
# c=[]
# for i in b:
#     if i<2:
#        c.append(i)
#     elif i==2:
#        None
#     else:
#        for x in range(2,i):
#           if i%x==0:
#              c.append(i)
# for i in b:
#    if i in c:
#       b.remove(i)
# print(b)
# 定义一个函数，传入一个数，判断该数字是否为素数
def get_prime(num):
    # 如果这个数字num能在小于它的数字里面找到一个数能和它整除，则不是素数
    for i in range(2, num):
        if num % i == 0:
            return False  # 如果不是素数，则返回False


# 这个ls就是就是目标列表，这里演示时，ls里面存放1-100的整数
a=input()
a=a.strip("[")
a=a.rstrip("]")
ls=[int(i) for i in a.split(",")]
# 将非素数放入一个列表当中
not_prime = []
# 将素数放入一个列表当中
is_prime = []

for i in ls:
    if i<2:
        not_prime.append(i)
    else: 
        get_prime(i)
        if  get_prime(i)== False:
           not_prime.append(i) # 非素数
        else:
            is_prime.append(i)  # 素数


print(is_prime)

