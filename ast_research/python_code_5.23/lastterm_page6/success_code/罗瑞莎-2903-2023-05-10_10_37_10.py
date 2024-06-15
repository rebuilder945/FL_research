def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e=1
    for i in range(num):
        e+=1/(i+1)
    print('%.6f'%e)
    
main()


