def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(x):
    e,t=1,1
    for i in range(1,x+1):
            t=t/i
            e+=t
    print('%.6F'%e)

main()


