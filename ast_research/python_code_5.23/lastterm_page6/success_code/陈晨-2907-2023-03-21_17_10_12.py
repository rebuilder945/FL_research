def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def  calculate_capital(a,b):
    for x in range(0,b):
        a+=a*0.003
    print("%.4f"%(a))

main()



