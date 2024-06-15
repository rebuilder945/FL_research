def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
        c = 1
        e = 1
        for i in range (1,num+1):
                c *= i
                e += 1/c
        print("%.6f"%e)
main()
main()


