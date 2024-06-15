def main():
    num = eval(input())
    calculate_e(num)
def  calculate_e(num): 
        n = int(num)
        e =1
        for i in range(1,n):
                m = 1
                for x in range(1,i+1):
                    m*=x+1
                e+=1/m
        e = e+1
        print('%.6f'%e)
                    
                    
main()


