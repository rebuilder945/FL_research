def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(n):
    e=1
    for i in range(1,n+1):
        fenmu =1
        for x in range(1,i+1):
           fenmu*=x
        e+=1/fenmu
    print(‘%.6f’%e)
main()


