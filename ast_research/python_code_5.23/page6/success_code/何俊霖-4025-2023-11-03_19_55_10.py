def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
        s=1
        for i in range(1,num+1):
            pi=1
            for x in range(1,i+1):
                pi=pi*x
            s=s+1/pi
        print("%.6f"%(s))
main()


