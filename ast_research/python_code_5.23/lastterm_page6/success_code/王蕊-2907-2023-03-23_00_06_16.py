def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
N=int()
p= N * (1.003)**M
print("%.4f"%(p))
main()



