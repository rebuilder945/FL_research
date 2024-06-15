def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
        e=1
        for i in range(1,num+1):
                y=1
                for x in range(1,i+1):
                        y*=x
                        a=1/y
                e=e+a
        print("%.6f"%(e))
main()


