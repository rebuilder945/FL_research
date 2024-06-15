def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    import math
    e=0
    m=0
    while m <= num:
        c=math.factorial(m)
        e+=1/c
        m+=1
    print('%.6f'%e)
main()


