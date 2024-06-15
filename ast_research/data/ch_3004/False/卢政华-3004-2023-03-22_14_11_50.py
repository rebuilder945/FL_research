def get_prime(num):
    # 如果这个数字num能在小于它的数字里面找到一个数能和它整除，则不是素数
    for i in range(2, num):
        if num % i == 0:
            return False  # 如果不是素数，则返回False


# 这个ls就是就是目标列表，这里演示时，ls里面存放1-100的整数
ls = input(list())
is_prime = []
print(is_prime)
