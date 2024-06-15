def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    m = 2
    for i in range(num-1):
        m = m+1/(i*i+3*i+2)
    print("%.6f"%(m))
main()


