def main():
    num = eval(input())
    calculate_e(num)
def  calculate_e(num):
    e=1
    for x in range(1,num):
         e=e+1/aa(x)
    print('%.6f'%e)
def aa(dd):
     if dd==1:
        return 1
     r=dd*aa(dd-1)
     return r  
main()


