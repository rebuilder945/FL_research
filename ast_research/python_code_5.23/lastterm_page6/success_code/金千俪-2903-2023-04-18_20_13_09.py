def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    fac = 1
    e = 1
    for n in range(1,num+1):
        fac*=n#阶乘
        e+=1/fac
    print("%.6f"%e)
main()


