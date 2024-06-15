def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e = 0
    t=1
    for x in range(num+1):
        for i in range(x+1):
            if i == 0:
                t = 1
            else:
                t *= i
        e+= 1/t     
    print(e)
main()


