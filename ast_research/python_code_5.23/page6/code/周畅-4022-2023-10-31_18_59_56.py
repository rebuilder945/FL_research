def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
       本金=(1+0.003)**M*N
       print(".4f%"% 本金)
main()



