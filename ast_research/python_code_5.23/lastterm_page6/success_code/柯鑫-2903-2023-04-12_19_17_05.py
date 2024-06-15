def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(m):
    a=1
    for x in range(1,m+1):
        b=1
        for y in range(1,b+1):
            b*=y
        a+=1/b
    print('%.6f'%a)
main()


