def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(x):
    n=1
    for i in range (1,x+1):
        m=1
        for j in range(1,i+1):
            m*=i
        n+=1/n
    print('%.6f'%n)
main()


