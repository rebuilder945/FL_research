def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
a=N
b=0.003
for i in range(M+1):
     a=a+a*b
main()



