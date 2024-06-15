def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(n):
    n1=1
    e=1
    for i in range(1,n+1):
        n1*=i
        e+=1/n1
    print("%.6f"%(e))

main()


