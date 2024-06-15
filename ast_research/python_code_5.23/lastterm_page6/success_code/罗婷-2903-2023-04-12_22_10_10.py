def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e=0
    m=1
    for i in range(1,num+1):
        for j in range(i):
            m=m*j
        e+=1/m
    print('%.6f'%e)
    
main()


