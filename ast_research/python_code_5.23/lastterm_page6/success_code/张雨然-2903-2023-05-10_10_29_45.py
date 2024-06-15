def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e=1
    for i in range(num):
        a=1
        for x in range(i+1):
            a*=(x+1)
        e+=1/a
    print('%.6f'%e)
main()


