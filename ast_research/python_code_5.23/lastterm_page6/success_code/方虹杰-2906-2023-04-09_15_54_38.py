def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_capital(N,M):    
    for i in range(M):
        N=N*0.003+N
    print("%.4f"%(N))
                
                
main()


