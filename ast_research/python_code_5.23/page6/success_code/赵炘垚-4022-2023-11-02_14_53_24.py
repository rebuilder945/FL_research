def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)

def calculate_capital(N,M):
    print(f"{_calculate_capital(N,M):.4f}")

def _calculate_capital(N,remainingYears):
    if remainingYears==0:return N
    return _calculate_capial(N*1.003,remainingYears-1)
main()



