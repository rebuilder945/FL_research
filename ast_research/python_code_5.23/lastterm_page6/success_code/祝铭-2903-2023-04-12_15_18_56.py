def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    m = 1
    n = 1
    e = 0
    for i in range(num):
        e += m
        m = 1/n
        n = n+1
    print("%.6f"%(e))
main()


