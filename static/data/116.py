def main():
    num = eval(input("请输入一个整数："))
    calculate_e(num)

def calculate_e(num):  # calculate_e() 函数定义了一个参数 num，但是在调用时没有传递参数,添加 num 参数
    e = 0
    for i in range(num):
        a = 1 / (i + 1)
        e += a
    print(e)

main()