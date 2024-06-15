def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e=1
    for i in range(num):
        a=1
        for x in range(num):
            x=x*(x+1)
            a+=a+x
        e+=1/a
    print('%.6f'%e)
    
main()


