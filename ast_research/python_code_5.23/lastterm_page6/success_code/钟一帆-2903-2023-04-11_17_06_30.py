def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
        e=1
        k=1
        for x in range(num):
                k*=x+1
                 
                e+=1/k
                
        print("%.6f"%e)        
main()


