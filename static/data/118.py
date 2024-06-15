def main():
    a = int(input("请输入一个整数："))
    calculate_sum(a)

def calculate_sum(a):
    lst = []
    a = str(a)
    lst.extend([a * (i + 1) for i in range(int(a))])
    #尝试将一个生成器表达式传递给 lst.append() 方法，
    #而 append() 方法只接受单个元素作为参数，而不是生成器，
    #可以使用列表推导式来创建一个列表，而不是生成器表达式。
    b = 0
    for x in lst:
        b = b + int(x)
    print(b)
        
main()
