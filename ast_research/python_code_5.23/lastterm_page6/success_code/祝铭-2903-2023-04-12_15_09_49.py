def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    m = 1
    for i in range(num):
        m = m+1/(i*i+i)
    print("%.6f"%(m))
main()


