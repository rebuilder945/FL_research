def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
    N,M=map(int,input().split())
    a=(1+0.003)**M
    b=N*a
    return b
N,M=eval(input())
print("%.4f"%calculate_capital(N,M))
main()



