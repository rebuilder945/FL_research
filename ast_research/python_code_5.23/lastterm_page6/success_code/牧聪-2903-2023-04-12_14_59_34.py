def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    m = 0
    e = 0
    for x in range(num+1):
        t = 1
        for i in range(x+1):
            if i == 0:
                t = 1
            else:
                t *= i
            m += 1/t
        e = m
    print(e)
main()


