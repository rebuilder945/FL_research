def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e=1
    x=1
    for i in range(num):
        e+=e/x
        x+=1
    h=e-1
    print("%.6f"%(h))
main()


