def main():
    num = int(input("Enter a number: "))
    calculate_e(num)

def calculate_e(n):
    t = 1
    m = 1
    for i in range(1, n + 1):
        m *= i
        t += m
    print("{:.6f}".format(t))

main()
#错误是由于 eval(input()) 返回的值太大，无法转换为浮点数所致。
