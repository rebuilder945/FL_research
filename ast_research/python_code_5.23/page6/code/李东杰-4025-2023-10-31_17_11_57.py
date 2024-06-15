def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e=2
    a=1
    for x in range(num-1):
        a=a*(x+2)
        b=1/a
        e+=b
print(“%.6f”%e)
main()


