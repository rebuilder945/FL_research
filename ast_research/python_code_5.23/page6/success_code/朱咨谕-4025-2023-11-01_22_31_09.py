def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
        e=0
        a=1
        for i in range(num+1):
                for j in range(1,i+1):
                        a*=j
                e+=1/a
                a=1
                
        print("%.6f"%e)
main()


