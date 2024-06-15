def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e = 1
    for i in range(num + 1):
        m = 1
        m *= (i + 1)
        if not m == 1: 
            e += 1/m
        else:
            pass
    print("%.6f"%e)
main()


