def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    s=1
    a=1
    for x in range(num):
        a=a/(x+1)
        s=s+a      
    print('%.6f'%(s))  
main()


