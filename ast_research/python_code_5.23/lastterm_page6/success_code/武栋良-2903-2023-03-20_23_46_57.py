def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    s = 1
    a = 1
    for i in range(1,num+1):
        for n in range(1,i+1):
            b = a*n
            a = b
        c = 1/b
        s = s+c
    print("%.6f"%(s))
main()


