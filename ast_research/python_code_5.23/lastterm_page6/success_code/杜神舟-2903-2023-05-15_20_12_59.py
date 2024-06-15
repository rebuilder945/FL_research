def main():
    num = eval(input())
    calculate_e(num)
def aa(x):
     if x==1:
        return 1
     r=x*aa(x-1)
     return r
def  calculate_e(num):
    e=1
    for x in range(num):
         e=e+1/aa(x)
    print('%.6f'%e)  
main()


