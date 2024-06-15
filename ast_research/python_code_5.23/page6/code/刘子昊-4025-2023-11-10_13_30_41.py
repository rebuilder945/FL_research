def main():
    num = eval(input())
    calculate_e(num)
       e=calculate_e(num)
       print('%.6f'%e)
def calculate_e(num):
    e=1
    x=1
    for i in range (1,num+1):
        x*=i
        e+=1/x
    return e

main()


