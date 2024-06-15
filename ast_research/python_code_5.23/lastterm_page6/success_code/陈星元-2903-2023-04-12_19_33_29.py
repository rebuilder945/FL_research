def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(n):
    e=1
    for x in range(1,n+1):
        m=1
        for i in range(1,x+1):
           m*=i
        e+=1/m
    print("%.6f"%e)
main()


