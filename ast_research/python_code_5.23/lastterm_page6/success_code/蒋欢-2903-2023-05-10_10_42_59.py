def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e=0
    for x in range(1,num+1):
        y=x**x
        e+=y
    print("%.6f"%e)
main()


