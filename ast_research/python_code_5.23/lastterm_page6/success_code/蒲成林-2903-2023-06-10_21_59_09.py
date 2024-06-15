def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
        e=1
        fac=1
        for i in range(1 , num+1):
                fac *= i
                e += 1/fac
        print(f"{N1:.6f}".format(e))
main()


