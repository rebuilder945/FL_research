def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
       for i in range(M):
             N *= 1.003
       print(f"{N:.4f}")
main()



