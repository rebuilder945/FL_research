def main():
    num = eval(input())
    calculate_e(num)
def  calculate_e(n):
        e=1
        t=1
        for x in range(1,n+1):
                t=t/x
                e=t + e
        print("%.6f"%e)
main()

main()


