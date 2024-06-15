def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
N=int()
M=input()
n=N / 1000
p=float( N * (1003)**M)
print("%.4f"%(p))
main()



