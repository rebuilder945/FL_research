def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(a,b):
    return print("%.4f"%(a*(1003/1000)**b))
main()



