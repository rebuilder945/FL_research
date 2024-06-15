def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
        if M>0:
            N==N*1.003
            M-=1
        else:
            return N
main()



