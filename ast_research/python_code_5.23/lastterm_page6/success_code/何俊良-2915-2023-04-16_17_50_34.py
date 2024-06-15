n = int(input().strip())# 读取一个整数

def is_Narcissus(number):
    """判断一个3位整数是否为水仙花数"""
    s = str(number)
    a = int(s[0]) ** 3
    b = int(s[1]) ** 3
    c = int(s[2]) ** 3
    narcissus_num = a + b + c
    if narcissus_num == number:
        return True
    else:
        return False

found_Narcissus = False  # 是否找到了水仙花数
for i in range(100, n+1):
    if is_Narcissus(i):
        found_Narcissus = True
        print(i)

if not found_Narcissus:
    print("none")

