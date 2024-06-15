def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
        s = 1
        for i in range(num):
                b = 1
                for a in range(i+1):
                      b *= a+1
                s+=1/b
        print('%.6f'%s)
main()


