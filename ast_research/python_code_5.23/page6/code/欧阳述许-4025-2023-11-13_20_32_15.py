def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(n):
   e,t=1,1
    for i in range(1,n+1):
            t=t/i
            e+=t
    print("%.6f"%e)
main()


