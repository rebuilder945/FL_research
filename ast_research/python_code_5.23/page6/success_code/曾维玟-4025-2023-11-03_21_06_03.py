def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(x):
    N=1
    for i in range(1,x+1):
        M=1
        for j in range(1,i+1):
            M*=j
            N=1/M
            print('%.6F'%N)

main()


