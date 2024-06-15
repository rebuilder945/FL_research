def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    a=1
    e=1
    b=1
    while a<=num:
        b=b*a
        a+=1
        e+=1/b
    print("%.6f"%e)
main()


