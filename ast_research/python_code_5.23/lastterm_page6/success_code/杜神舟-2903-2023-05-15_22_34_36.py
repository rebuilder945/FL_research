def main():
    num = eval(input())
    calculate_e(num)
def  calculate_e(num):
    e=1
    if num>10:
         e=2.718282
         print('%.6f'%e)
    else:
        for x in range(1,num+1):
          e=e+1/aa(x)
          print('%.6f'%e)

def aa(dd):
     if dd==1:
        return 1
     r=dd*aa(dd-1)
     return r  
main()


