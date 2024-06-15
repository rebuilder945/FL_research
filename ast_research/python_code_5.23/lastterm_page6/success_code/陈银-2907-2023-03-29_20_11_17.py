def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(a,b):
    c= float(0.003)
    d = a*(1+c)**b
    print("%.4f"%(d))
main()



