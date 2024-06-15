def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
  def  calculate_capital(N,M):
    a=(1.003)**M*N
print('%.4f'%a)

main()



