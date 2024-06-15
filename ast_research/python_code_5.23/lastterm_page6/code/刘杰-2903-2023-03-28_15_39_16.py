def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(x):
    n=1
    for i in range (1,x+1):
        n+=1/i!
    print('%.6f'%n)
main()


