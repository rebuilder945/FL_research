def main():
    num = eval(input())
    calculate_e(num)
def  calculate_e(num):
    s=1
    m=1
    for i in range(num+1):
        s=s*(i+1)
        m=m+1/s
    print("%.6f"%m)

main()


