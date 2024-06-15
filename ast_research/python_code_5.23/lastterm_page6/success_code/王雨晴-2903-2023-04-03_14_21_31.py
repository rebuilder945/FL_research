def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    a=1
    for x in range(num):
        b=1
        for y in range(x+1):
            b*=y+1
        a+=1/b
    print('%.6f'%a)
main()


