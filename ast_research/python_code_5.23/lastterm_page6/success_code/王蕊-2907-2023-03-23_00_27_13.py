def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
N=int()
M=input()
n=N / 1000
m=eval(input(M))
p=float( n* (1003**m))
print("%.4f"%(p))
main()



