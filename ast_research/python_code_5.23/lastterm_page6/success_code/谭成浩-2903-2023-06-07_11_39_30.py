def main():
    num = eval(input())
    calculate_e(num)
def jie(n):
    m=1 
    for i in range(n):
        m*=i+1
    return 1/m
def calculate_e(x):
    g=1
    for i in range(x):
        g+=jie(i+1)
    print('%.2f'%(g)) 

main()


