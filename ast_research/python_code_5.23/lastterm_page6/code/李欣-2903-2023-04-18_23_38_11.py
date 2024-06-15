def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(x):
        m=1
        for i in range(1,x+1):
             s=1
             for j in range(1,i+1):
                  s=j*s
             m=1/s
       print("%.6f".%m)
main()


