def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
N = calculate_capital(N,M)
    print("%.4f"%N)
    def calculate_capital(a,b):
        times = 0
        while times !=b:
            a = 1.003*a
            times+=1
        return a
main()



