def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(a):
    m=1
    while a>0:
        m=m*1/a+1
        a=a-1
    print("%.6f"%m)
main()


