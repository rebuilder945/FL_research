def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
    print(f"{_calculate_capital(N,M):.4f}")
def calculate(N,M):
    if M==0:return N
    else:
    return calculate(N*1.003,M-1)
main()



