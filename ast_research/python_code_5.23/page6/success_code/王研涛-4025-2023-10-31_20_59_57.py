def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(e):
    a=1
    for i in range(1,e+1):
            x=1
            for l in range(1,i+1):
                x=x*l
            a=a+(1/x)
    print("%.6f"%a)
main()


