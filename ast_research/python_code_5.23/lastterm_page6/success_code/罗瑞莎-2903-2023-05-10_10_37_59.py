def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e=1
    a=1
    for i in range(num):
        a*=i+1
        e+=1/a
    print('%.6f'%e)
    
main()


