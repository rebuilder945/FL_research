def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(a):
    e=0
    for i in range(a+1):
        for x in range(i+1):
            num *=x
        e+=1/num
    print('%.6f'%e)
main()


