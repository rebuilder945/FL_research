def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(a,b):
    money = a*(1 + 0.003)**b
    print("%.4f"%(money))
main()



