def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e=1
    for x in range(num):
        e=e+1/(x+1)!
    print('%.6f'%e)
main()


