def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(n,m):
    a = [n]
    for x in range(m):
        b = a[-1]*1.003
        a.append(b)
    print('%4.f'%(a[-1]))
main()



