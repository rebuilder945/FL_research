def main():
    num = eval(input())
    calculate_e(num)

def calculate_e(num):
    e=0
    a=1
    for i in range(num):
        e+=1/a
        a=a*(i+2)
    print("%.6f"%e)

main()


