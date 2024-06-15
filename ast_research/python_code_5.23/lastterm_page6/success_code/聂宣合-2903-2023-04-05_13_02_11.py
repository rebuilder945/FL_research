def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    
    times=0
    dex=1
    sum=0
    for i in range(1,num+1):
        dex=float(dex*i)
        middle=1/dex
        sum=sum+middle
        times=times+1
        if times==num:
            print("%.6f"%(sum+1))

main()


