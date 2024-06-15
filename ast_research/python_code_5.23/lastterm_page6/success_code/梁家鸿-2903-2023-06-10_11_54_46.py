def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e = 1
    a = 1
    for x in range(num):
        a = a * (1/(x+1))
        e +=a
    print("%.6f"%e)
main()


