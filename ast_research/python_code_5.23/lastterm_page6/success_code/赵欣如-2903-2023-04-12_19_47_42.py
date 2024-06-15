def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
        e=1
        for i in range (1,int(num)+1):
                a=1
                for n in range(1,i+1):
                        a=a*n
                b=1/a
                e+=b
        print("%.6f"%e)
main()


