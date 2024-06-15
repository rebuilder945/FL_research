def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    i = 1
    n = 1
    e = 1
    for x in range(num):
        n *= i
        e += 1 / n
        i += 1
    print("%.6f"%(e))
main()


