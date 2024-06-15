def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(x):
    a=1
    for i in range(1,x+1):
        b=1
        for j in range(1,j+1):
            b*=j
        a+=1/b
    print('%.6f'%a)
main()


