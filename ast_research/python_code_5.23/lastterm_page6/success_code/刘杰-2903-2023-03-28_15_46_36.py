def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(x):
    n=m=1
    for i in range (1,x+1):
        n*=i
        n+=1/n
    print('%.6f'%n)
main()


