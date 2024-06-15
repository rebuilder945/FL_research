def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(a):
    b=1
    c=1
    for i in range(a):
        b=b*(i+1)
        c=c+1/b
    print("%.6f"%c)
main()


