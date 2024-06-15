def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    m = 1
    for i in range(num):
        n = 1
        for j in range(num):
            n = n*(j+1)
        m = m+1/n
    print("%.6f"%(m))
main()


