def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
        e=1
        for i in range(num):
                x=i+1
                c=1
                while x>=1:
                       c=c/x
                       x=x-1
                e=e+c
        print("%.6f"%(e))
main()


