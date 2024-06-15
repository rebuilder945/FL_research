def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
       def calculate_capital(n,m):
    sum=n
    for x in range(m):
        sum*=1.003
    print("%.4f"%sum)
main()



