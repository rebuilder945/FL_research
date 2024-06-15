def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e=0
    m=1
    for i in range(num):
        for j in range(i+1):
            m=m*(j+1)
        e+=1/m
    print('%.6f'%e)
    
main()


