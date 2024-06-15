def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(n):
    e=1
    for i in range(n):
        b=1
        for x in range(i+1):
            b=b*(x+1)
        e=e+1/b
    print("%.6f"%e)
main()


