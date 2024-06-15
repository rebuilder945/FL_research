def main():
    num = eval(input())
    calculate_e(num)
    print('%.6f'%calculate_e(num))
def calculate_e(num):
    e=1
    n=1
    for i in range(2,num+2):
        e=e+1/n
        n=n*i
    return e
        

main()


