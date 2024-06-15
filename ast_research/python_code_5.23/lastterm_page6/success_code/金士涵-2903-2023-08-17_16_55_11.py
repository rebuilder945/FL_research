def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    n=1
    e=1
    for i in range(1,num+1):
        n = i*n
        e = e+1/n
    print("%.6f"%e)

main()


